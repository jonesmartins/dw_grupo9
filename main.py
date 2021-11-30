import os
import shutil
import sys

from analysis.graph_analysis import generate_plots

import sqlite3

from database.create_database import create_schema
from database.load_data_into_base import load_data
from dictionaries.paths_dict import database_root_path, source_data_csv, rootpath, data_root_path, \
    source_data_root_path, schema_script_path
from download.get_data_from_web import get_data
from download.merge_csv_files import merge_csvs


def check_if_file_exists(path):
    return os.path.exists(path)


def start_connection():
    print('Starting connection')
    return sqlite3.connect(database_root_path)


def end_connection(connection):
    print('Closing connection')
    connection.close()


def run_process():
    if not check_if_file_exists(source_data_root_path):
        get_data()
        merge_csvs()
    else:
        print(f"csv files already exists: {source_data_root_path}, ignoring")

    if not check_if_file_exists(database_root_path):
        print('Starting connection')
        connection = sqlite3.connect(database_root_path)
        create_schema(connection, schema_script_path)
        print('Closing connection')
        connection.close()
    else:
        print(f"db already exists: {database_root_path}, ignoring creation")

    if check_if_file_exists(database_root_path):
        connection = start_connection()
        try:
            load_data(connection.cursor(), source_data_csv)
            connection.commit()
        except sqlite3.Error as er:
            error_string = ' '.join(er.args)
            print(error_string)
            is_unique_error = error_string.lower().find("unique") != -1
            if is_unique_error:
                print('DB is already filled up')
        generate_plots(connection.cursor())
        end_connection(connection)
    else:
        raise Exception(f"db don't exist: {database_root_path}, aborting")


def delete_data():
    print('Reseting all process by deleting /data folder')
    shutil.rmtree(data_root_path, ignore_errors=True)
    print('Reseting finished')


if __name__ == '__main__':
    argument = sys.argv[1] if len(sys.argv) == 2 else None
    if argument == "reset":
        delete_data()
    # elif argument == "learn":
    #     run_only_learning()
    else:
        run_process()
