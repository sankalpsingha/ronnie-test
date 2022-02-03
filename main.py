import os
import re
import shutil
from art import tprint
import sys
from getpass import getpass

def create_folder():
    if os.path.isdir('updated'):
        print("Folder already exists.. Deleting the folder")
        shutil.rmtree('updated')
    print('Creating the updated folder..')
    os.mkdir('updated')

def main(foldername):
    folder = foldername
    if not os.path.isdir(folder):
        print(f"No such folder: {folder} \nExiting")
        sys.exit(0)
    os.chdir(folder)
    cool_list = []
    list_of_files = sorted( filter( lambda x: os.path.isfile(os.path.join(folder, x)),
    os.listdir(folder) ) )
    create_folder()
    for file_name in list_of_files:
        if file_name == 'main.py' or file_name == '.DS_Store':
            continue
        cool_list.append(file_name)
   
    for count, filename in enumerate(cool_list):
        shutil.copy(f"{filename}", f"updated/{filename[:-9]} {count+1}.pdf")

if __name__ == '__main__':
    tprint("Sankalp is awesome")
    code = getpass("enter code: ")
    if (code != '1908'):
        print('Wrong code. Exiting')
        sys.exit(0)
    if len(sys.argv) == 1:
        print("You did not add the directory. Exiting")
        sys.exit(0)
    main(sys.argv[1])