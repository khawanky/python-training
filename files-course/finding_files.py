import os, fnmatch
from pathlib import Path

def list_dir(fld):
    for fn in os.listdir(fld):
        print(fn)

def end_with(fld, search):
    for fn in os.listdir(fld):
        if fn.endswith(search):
            print(fn)

def start_with(fld, search):
    for fn in os.listdir(fld):
        if fn.startswith(search):
            print(fn)

def match(fld, search):
    for fn in os.listdir(fld):
        if fnmatch.fnmatch(fn, search):
            print(fn)

def glob_match(fld, search):
    p = Path(fld)
    for n in p.glob(search):
        print(n)

# list_dir("./files")
# end_with("./files", ".txt")
# start_with("./files", "01_test")
# match("./files", "*_file.csv")
# match("./files", "*_file_.*")
# glob_match("./files", "*2*.t*")
# glob_match("./files/subfolder", "*_file_*.t*")
