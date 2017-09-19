import os
import re
from shutil import copyfile

def main():

    # get all static files' path
    static_files = []
    parent_path = "./content" # find static files below
    sub_dirs = ['/'.join((parent_path, name)) for name in os.listdir(parent_path) \
        if os.path.isdir('/'.join((parent_path, name)))]

    for sub_dir in sub_dirs:
        static_files.extend(traverse(sub_dir))

    print('Number of static files: {}'.format(len(static_files)))


    # copy all static files into
    target_path = './content/images'
    for f in static_files:
        copyfile(f, '/'.join((target_path, re.sub(r'.*/images/', '', f))))


def traverse(path):
    """
    Traverse all sub directories in given path and return all static files'
    path.
    """
    sub_dirs = ['/'.join((path, name)) for name in os.listdir(path) \
        if os.path.isdir('/'.join((path, name)))]
    static_files = []



    for sub_dir in sub_dirs:
        if '/images' in sub_dir:
            static_files.extend(get_static_file_names(sub_dir))
        elif '/datasets' in sub_dir:
            pass
        else:
            static_files.extend(traverse(sub_dir))

    return static_files


def get_static_file_names(path):
    """
    Return all file name in given path.
    Assume there is no more folders in current path.
    """
    return ['/'.join((path, name)) for name in os.listdir(path) if not name.startswith('.')]


if __name__ == "__main__":
    main()
