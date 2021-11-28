
from download.get_data_from_web import get_data
from dictionaries.paths_dict import source_data_root_path, urls, database_root_path
from database.create_database import create_schema

import csv
import sqlite3

if __name__ == '__main__':
    # Salva tabelas em data/source_data/
    get_data()

    # Une CSVs
    filenames = list(urls.keys())

    filename1 = '/'.join([source_data_root_path, filenames[0]])
    filename2 = '/'.join([source_data_root_path, filenames[1]])
    filename3 = '/'.join([source_data_root_path, 'joined.csv'])

    with open(filename1, mode='r') as file1:
        with open(filename2, mode='r') as file2:
            csvreader1 = csv.DictReader(file1)
            csvreader2 = csv.DictReader(file2)

            header1 = csvreader1.fieldnames
            print(header1)
            header2 = csvreader2.fieldnames
            print(header2)
            header3 = header1 + header2[4:]
            print(header3)



            with open(filename3, mode='w') as file3:
                writer = csv.DictWriter(file3, fieldnames=header3)
                writer.writeheader()
                for row1, row2 in zip(csvreader1, csvreader2):
                    row1.update(row2)
                    writer.writerow(row1)

    print('Starting connection')
    connection = sqlite3.connect(database_root_path)
    create_schema(connection, 'database_schema.sql')
    cursor = connection.cursor()

    from database import load_data_into_base.lo

    load_data(cursor, filename3)






    print('Closing connection')
    connection.close()
