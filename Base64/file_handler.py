import json
from Base64.path_handler import *


def write_to_json(file_path="", data={}, encoding="ascii"):
    json.dump(data, open(file_path, mode="w+", encoding=encoding), indent=4)


def write_to_bin(file_path="", data=b""):
    with open(file_path, "wb") as file:
        file.write(data)


def write_to_file(file_path="", data=[], create_new_file=True):
    """
    Write Data to a File, either overwriting the existing file or creating a new file at the given path.
    :param file_path: Current Path of the File
    :param data: Data to Write
    :param create_new_file: Create a new File Flag
    :return:
    """
    file_path = new_file_path(file_path) if create_new_file else file_path
    with open(file_path, mode="w+") as file:
        for element in data:
            file.write(element + "\n")
            file.newlines()
