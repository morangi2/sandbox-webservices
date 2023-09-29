#!/usr/bin/env python3

import os
import requests
import json

feedback_dict_keys = ["title", "name", "date", "feedback"]
feedback_dict = []
feedback_folder_path = "/uSERS/EVEMWANGI/PYTHON_ANDTHE_OS/CAPSTONE/feedback"
host_url = "http://ipaddress/feedback/"
file_src_dir = "/data/feedback/"

#instructions
# List all .txt files under /data/feedback directory that contains the actual feedback to be displayed on the company's website.
# HINT: Use os.listdir() method for this, which returns a list of all files and directories in the specified path.

#capture list of files
files = os.listdir(file_src_dir)

#read file lines into a list
def readeachfile(file):
    with open(file_src_dir + file) as f:
        lines = f.read().splitlines()
    return lines

#load feedback entries into dctionary
for file in files:
    lines = readeachfile(file)
    feedback_dict.append(dict(zip(feedback_dict_keys, lines)))

#post feedback entries
for eachentry in feedback_dict:
    response = requests.post(host_url, data = eachentry)
    if response.ok:
        print("SUCCESS!")
    else:
        print("Error! " + response.status_code)
