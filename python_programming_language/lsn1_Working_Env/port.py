#port.py
#Rewrite code to use csv module for data inport and cleaning at higher level

import csv

total = 0.0

with open('portfolio.csv', 'r') as f:
    rows = csv.reader(f)
    headers = next(rows)           #skip a single line of input to accomodate header row
    for row in rows:
        row[2] = int(row[2])
        row[3] = float(row[3])
        total += row[2]*row[3] #Total shares x total price
        print('{:>5s} {:>10f}'.format(row[0],total))

print('Total cost:', total)


#learning step 2 - reading code in and stripping data manually
#total = 0.0
#
#with open('portfolio.csv', 'r') as f:
#    headers = next(f)           #skip a single line of input to accomodate header row
#    for line in f:
#        line = line.strip()     #strip whitespace
#        parts = line.split(',') #make list
#        parts[0] = parts[0].strip('"')
#        parts[1] = parts[1].strip('"')
#        parts[2] = int(parts[2])
#        parts[3] = float(parts[3])
#        total += parts[2]*parts[3] #Total shares x total price
#        print('{:>5s} {:>10f}'.format(parts[0],total))
#
#print('Total cost:', total)


#f = open('portfolio.csv', 'r')
#for line in f:
#    print(line)

