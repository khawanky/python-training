import os, zipfile, shutil, working_with_files_folders

def zip_files_inside_folder(fld):
    to_zip_full_path = []
    for fld_path, dirs, files in os.walk(fld):
        fld_path_str: str =fld_path
        fld_path_str = fld_path_str.replace('\\','/')
        for fn in files:
            to_zip_full_path.append(f"{fld_path_str}/{fn}")

    folder_zip_name = fld + '.zip'
    create_zip(folder_zip_name, to_zip_full_path, 'w')

def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for f in files:
            archive.write(f)

def read_zip(zipf):
    with zipfile.ZipFile(zipf, 'r') as archive:
        lst = archive.namelist()
        for f in lst:
            zfinf = archive.getinfo(f)
            print(zfinf)

def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extract(fn, path=path)

def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extractall(path=path)



# TODO: This is buggy, need to be fixed
# zip_files_inside_folder('./files/subfolder')

# read_zip('./files/subfolder.zip')
# extract_file('./files/subfolder.zip', 'files/subfolder/01_test_file.csv', 'extracted')
# extract_all('./files/subfolder.zip', 'extracted')

