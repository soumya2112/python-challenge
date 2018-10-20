#Import the os module
#To create file across operating systems.
import os 

# Module for reading .csv files
import csv

with open('budget_data.csv', 'rt') as csvfile:
    csvreader = csv.reader(csvfile , delimiter = ',')
    row = next(csvreader)
    print(row)
    row = next(csvreader)
    print(row)


