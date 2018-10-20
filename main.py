#Import the os module
#To create file across operating systems.
import os 

# Module for reading .csv files
import csv

csvpath = 'budget_data.csv'
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile , delimiter = ',')
    for row in csvreader:
        print(row)
   


