# 01/14/2025
# Shuiming Chen

# import pandas to print data
import pandas as pd

# get the data path
file_path = "./data/Iris.csv"

# get the data and print out
data = pd.read_csv(file_path)
print(data)


'''
import csv

# get the data path
file_path = "./data/Iris.csv"

# open and read the file
with open(file_path, mode='r') as f:
    csv_lines = csv.reader(f)

    # print out the data line by line
    for row in csv_lines:
        print(row)
'''