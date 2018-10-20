#Import the os module
#To create file across operating systems.
import os 

# Module for reading .csv files
import csv

with open('budget_data.csv', 'rt') as csvfile:
    data = []
    for r in csv.reader(csvfile , delimiter = ','):
        data.append(r)

data = data[1:]

for d in data:
    d[1] = int(d[1])

total = 0
for d in data:
    total = total + d[1]

prev_profit = data[0][1]
max_incr = None
max_decr = None
max_data = None
min_data = None
for d in data[2:]:
    diff = d[1]- prev_profit
    if max_incr is None or diff > max_incr:
        max_data = d
        max_incr = diff
    if max_decr is None or diff < max_decr:
        min_data = d
        max_decr = diff
    prev_profit = d[1]

out = []
out.append('Financial Analysis:')
out.append('------------------:')
out.append('Total Months: %d' % len(data))
out.append('Total: $%d' % total)
out.append('Greatest Increase in Profits: %s ($%s)' % (max_data[0], max_incr))
out.append('Greatest Decrease in Profits: %s ($%s)' % (min_data[0], max_decr))

with open('output.txt', 'wt') as outfile:
    for line in out:
        print(line)
        outfile.write(line + '\n')
