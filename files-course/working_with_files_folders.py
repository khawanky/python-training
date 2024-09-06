import os, shutil
from datetime import datetime
from os import remove
from pathlib import Path

def get_date(timestamp):
    return datetime.utcfromtimestamp(timestamp).strftime('%d %b %Y')

def get_file_attrs(fld):
    with os.scandir(fld) as dir_to_check:
        for f in dir_to_check:
            if f.is_file():
                inf = f.stat()
                print(f"Modified {get_date(inf.st_mtime)} {f.name}")

def traverse(fld):
    for fld_path, dirs, files in os.walk(fld):
        print(f"Folder: {fld_path}")
        print(f"\tDirs: {dirs}")
        for fn in files:
            print(f"\t{fn}")

def copy_file(src, dst):
    shutil.copy(src, dst)

def copy_folder(src, dst):
    shutil.copytree(src, dst)

def move_files(src, dst):
    shutil.move(src, dst)

def rename_file_1(src, dst):
    os.rename(src, dst)

def rename_file_2(src, dst):
    f = Path(src)
    f.rename(dst)

def remove_file(file):
    if os.path.isfile(file):
        try:
            os.remove(file)
            print(f"File: {file} removed")
        except OSError as os_error:
            print(f"Error: {file} {os_error.strerror}")
    else:
        print(f"Error: {file} is not a file or it doesn't exist")

def remove_folder_and_its_contents(fld):
    if os.path.isdir(fld):
        try:
            shutil.rmtree(fld)
            print(f"Folder: {fld} and all its content removed")
        except OSError as os_error:
            print(f"Error: {fld} {os_error.strerror}")
    else:
        print(f"Error: {fld} is not a folder or it doesn't exist")

# get_file_attrs('./files/subfolder')
# copy_file('./files/02_file.txt','./files/subfolder')
# copy_folder('./files','./files/new_folder')
# move_files('./files/text.txt','./files/subfolder/text.txt')
# move_files('./files','./xyz')
# move_files('./xyz','./files')
# rename_file_1('./files/new_folder/text.txt', './files/new_folder/test.txt')
# rename_file_2('./files/new_folder/test.txt','./files/new_folder/text.txt')
# remove_file('./files/new_folder')
# remove_folder_and_its_contents('./files/new_folder')

# traverse('./files')

