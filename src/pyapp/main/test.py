'''
Created on 2020. 7. 8.

@author: solom
'''
# -*- Encoding:utf-8 -*-

# code.py
# Link:https://code.i-harness.com/ko/q/6e87e6
from requests import get  # to make GET request

def download(url, file_name):
    with open(file_name, "wb") as file:   # open in binary mode
        response = get(url, params=None)               # get request
        print()
        print(response)
        file.write(response.content)      # write to file

if __name__ == '__main__':
    url = "https://drive.google.com/u/0/uc?id=1FmMw9AcNVrUEN8CiPauefBKVBTblP6ST&export=download"
    download(url,"test.jar")
