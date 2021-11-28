import sqlite3

from database.create_database import create_schema
from database.load_data_into_base import load_data
from dictionaries.paths_dict import database_root_path, source_data_csv, rootpath
from download.get_data_from_web import get_data
from download.merge_csv_files import merge_csvs

if __name__ == '__main__':
    get_data()
    merge_csvs()
    print('Starting connection')
    connection = sqlite3.connect(database_root_path)
    create_schema(connection, f"{rootpath}/database/database_schema.sql")
    cursor = connection.cursor()
    load_data(cursor, source_data_csv)
    connection.commit()
    print('Closing connection')
    connection.close()
