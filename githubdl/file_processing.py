import pathlib
import os
import logging

def get_target_full_filename(file_name, target_path):
    modified_path = get_filename_without_first_directory(file_name)
    full_file_name = os.path.join(target_path, modified_path)
    return full_file_name

def get_filename_without_first_directory(file_name):
    path = pathlib.Path(file_name)
    return str(pathlib.Path(*path.parts[1:]))

def write_file(file_name, file_data):
    logging.info("Writing to file: " + file_name)
    with open(file_name, 'wb') as write_file:
        write_file.write(file_data)

def create_directory(dir_name):
    logging.info("Checking for directory: " + dir_name)
    if not os.path.exists(dir_name):
        logging.info("Creating directory: " + dir_name)
        os.makedirs(dir_name)
