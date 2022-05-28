# -*- coding: utf-8 -*-
"""
Created on Fri May 20 21:08:59 2022

@author: Marcus Herstik

Description: This is a project to check about house price data in the UK.
"""


# Python Libraries for handling numeric computation and dataframes
import pandas as pd
import numpy as np



# Reading the data in a variable
# The data is stored in personal Github repository
# https://github.com/Mherstik/COMP6004pub/raw/main/UK-HPI-full-file-2021-04.csv

########
#
# # Consider downloading and saving to local
from urllib import request
from tqdm import tqdm
import os
# Define the remote file to retrieve
url = 'https://github.com/Mherstik/COMP6004pub/raw/main/UK-HPI-full-file-2021-04.csv'
# # Define the local filename to save data
local_file = 'UK-HPI-full-file-2021-04.csv'

my_dir = '.'# enter the dir name
file_exists = os.path.exists(local_file)
# print(file_exists)
# for fname in os.listdir(my_dir):
#     if fname.startswith("UK-HPI-full-file"):
#         print("File exists")
#         break
#     else: 

class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)

def download_url(url, local_file):
    with DownloadProgressBar(unit='B', unit_scale=True,
                             miniters=1, desc=url.split('/')[-1]) as t:
        request.urlretrieve(url, filename=local_file, reporthook=t.update_to)

# # Download remote and save locally
if file_exists == False:
        print("File does not exist.\r\nDownload it?")
        dwn = input("Yes or no: ")
        if dwn.lower() == "y" or dwn.lower() == "yes":
            # request.urlretrieve(url, local_file)
            download_url(url, local_file)
        else:
            print("Not downloaded.")
else:
    print("File exists")
#
########
# Note: The file is 54MB+ in size
# df = pd.read_csv("https://github.com/Mherstik/COMP6004pub/raw/main/UK-HPI-full-file-2021-04.csv")

df = pd.read_csv("UK-HPI-full-file-2021-04.csv")

# Checking basic dataset information, such as data types and dimensions, etc.

df.info()
df.shape()