#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

PASS = "123"

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
    with open("theKey.key", "rb") as Key:
        key = Key.read()
        return key

def decrypt(start_path, key):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file == "enc.py" or file == "theKey.key" or file == "dec.py" or file == ".env":
                continue
            file_path = os.path.join(root, file)
            if os.path.isfile(file_path):
                with open(file_path, "rb") as File:
                    contents = File.read()
                    # print(contents)
                    contents_decrypted = Fernet(key).decrypt(contents)
                with open(file_path, "wb") as File:
                    File.write(contents_decrypted)

def check(PASS):
    entered_pass = input("Enter the pass to decrypt: ")
    return PASS == entered_pass

key = get_key()  

files_list = list_files("./")

# print(files_list)

if check(PASS):
    decrypt("./", key)
    print("Decryption succesful")
else:
    print("Wrong pass. Try Again")
