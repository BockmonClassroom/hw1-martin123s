# 01/14/2025
# Shuiming Chen


import csv

# get the data path
file_path = "./data/Iris.csv"

# open and read the file
with open(file_path, mode='r') as f:
    csv_lines = csv.reader(f)

    # print out the data line by line
    for row in csv_lines:
        print(row)
