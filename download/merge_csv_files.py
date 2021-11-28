import csv

from dictionaries.paths_dict import urls, source_data_root_path, source_data_csv

def merge_csvs():
    filenames = list(urls.keys())
    filename1 = '/'.join([source_data_root_path, filenames[0]])
    filename2 = '/'.join([source_data_root_path, filenames[1]])

    with open(filename1, mode='r') as file1:
        with open(filename2, mode='r') as file2:
            csvreader1 = csv.DictReader(file1)
            csvreader2 = csv.DictReader(file2)

            header1 = csvreader1.fieldnames
            header2 = csvreader2.fieldnames
            header3 = header1 + header2[4:]

            with open(source_data_csv, mode='w') as file3:
                writer = csv.DictWriter(file3, fieldnames=header3)
                writer.writeheader()
                for row1, row2 in zip(csvreader1, csvreader2):
                    row1.update(row2)
                    writer.writerow(row1)