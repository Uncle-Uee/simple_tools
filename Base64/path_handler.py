import os


def get_extension(filename=""):
    extension = filename[filename.index('.'):]
    return extension


def get_filename(path="", omit_extension=False):
    filename = os.path.basename(path)
    return filename[:filename.index('.')] if omit_extension else filename


def new_file_path(path):
    filename = os.path.basename(path)
    extension = get_extension(filename)
    path = os.path.join(os.path.dirname(os.path.abspath(path)), f"new_{filename}{extension}")
    return path


def get_path_to_all_files(path=os.getcwd(), ignore_files=[], ignore_extensions=[]):
    list_of_files = []
    for (directory_path, directory_names, filenames) in os.walk(path):
        list_of_files += [os.path.join(directory_path, file) for file in filenames if file not in ignore_files
                          and get_extension(file) not in ignore_extensions]
    return list_of_files


def get_path_to_cwd_files(path=os.getcwd(), ignore_files=[], ignore_extensions=[]):
    return list(file for file in os.listdir(path) if
                os.path.isfile(file) and file not in ignore_files and get_extension(file) not in ignore_extensions)


def get_paths_of_files(path=os.getcwd(), ignore_files=[], ignore_extensions=[], include_sub_directories=False):
    return get_path_to_all_files(path, ignore_files, ignore_extensions) if include_sub_directories \
        else get_path_to_cwd_files(path, ignore_files, ignore_extensions)
