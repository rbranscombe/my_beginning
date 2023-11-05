#This program shows how you might read a file containing colums of data seperated by commas:

import csv

#File containing lines of the form "name, shares, price"
filename = 'portfolio.csv'

headers = ['Symbol', 'Shares', 'Price']
stock_list1 = ['AA', '100', '32.2']
stock_list2 = ['IBM', '50', '91.1']

with open(filename, 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter = ',')
    filewriter.writerow(headers)
    filewriter.writerow(stock_list1)
    filewriter.writerow(stock_list2)
        
#The resulting portfolio list created by this program looks like a 2-dimensional array of rows and columns.  Each row is represented by a tuple and can be accessed as follows:

#total = 0.0

#for name, shares, prince in portforlio:
#    total += shares * price
    
