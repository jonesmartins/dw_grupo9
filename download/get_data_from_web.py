import errno
import os
import requests
import zipfile
from dictionaries.paths_dict import (
    curr_dir,
    data_root_path,
    source_data_root_path,
    database_root_path,
    urls,
)


def split_file_name(uri):
    splitted_path = str(uri).split("/")
    return '/'.join(splitted_path[0:-1]), splitted_path[-1]


def open_or_create_file(directory, file_name):
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    return open('/'.join([directory, file_name]), 'wb')


def download_file(url, directory, save_as):
    print('Downloading {0} to {1}'.format(url, directory))
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open_or_create_file(directory, save_as) as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    print(f'Finished downloading {save_as} from {url}')


def get_data():
    for filename, url in urls.items():
        download_file(url, source_data_root_path, save_as=filename)


if __name__ == '__main__':
    get_data()
