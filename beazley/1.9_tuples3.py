#! /usr/bin/env python3

#First I made a file called porfolio.csv with python code in typles2.py

#Now make a program that reads in a csv file

#File containing lines of the form "name,shares,price"

import csv

filename = 'portfolio.csv'

portfolio = []
with open(filename, 'r') as file:
    csv_reader = csv.reader(file)

    header = next(csv_reader)
    print(header)    
    for line in csv_reader:
        name = line[0]
        shares = int(line[1])
        price = float(line[2])
        holding = (name, shares, price)
        print(holding) 
        portfolio.append(holding)
        #you can also create a set using a set comprehenion Section 1.10 - for example
        #this statement turns all the stock names from the data in the previous section into
        #a set
        names = { s[0] for s in portfolio }
        print(f'names set is {names}')

#Portfolio list is created as 2 dimentional array of rows and columns
print(f'portfolio is {portfolio[0]}')
print(f'data inside column 1 is {portfolio[0][0]}')
print(f'data inside column 2 is {portfolio[0][1]}')
print(f'data inside column 3 is {portfolio[0][2]}')


#Method 1
#write a loop through the array to get a total for networth in portfolio

#Toggle Method value to 1 or not 1 to test code
Method = 0
if Method == 1:


    total = 0
    for name, shares, price in portfolio:
        total += shares * price
    print(f'Total is ${total:0.2f}')
    


#Method 2
#write a list comprehension to do same thing - just 

else:
    total = sum([shares*price for _, shares, price in portfolio])
    print(f'total is ${total:0.2f}')

    #here when iterating over tuples, the variable _ can be used to indicate a discarded value in the above calculation it means that we are ignoring the first item which is name

      
        

