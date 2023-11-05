#port2.py
#Modify file reader to be generic using function - exercise 5.2

import csv

def read_portfolio(filename, *, errors='warn'):
    '''
    Read a CSV file with name, date, shares and price data into a list.
    '''
    
    if errors not in { 'warn', 'silent', 'raise' }:
        raise ValueError("Errors must be one of 'warn', 'silent', 'raise'")
    
    portfolio = []   # make empty list initialise list of records

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)           #skip a single line of input to accomodate header row
        #rowno = 1                      replace with enmumerate function
        for rowno, row in enumerate(rows, start=1): #enumerate function allows builtin counter
            #rowno += 1                 replace with enumerate function
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
               
            except ValueError as err:  #write exception ValueError reason to variable err
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row:', row)
                    print('Row:', rowno, 'Error Reason:', err)
                elif errors == 'raise':
                    raise              #reraises the last exception
                else:
                    pass               #ignore
                continue               #skips to next row
            #record = tuple(row) replace record tuple with a dictionary to make code more robust
            record = {
                'name': row[0],
                'date': row[1],
                'shares': row[2],
                'price': row[3]
                }
            portfolio.append(record)
        return portfolio 

portfolio = read_portfolio('portfolio.csv')
print(portfolio)

total = 0.0
for items in portfolio:
    total += items['shares']*items['price']

print('Total cost:', total)


#total = 0.0                         if code used tuple - uncomment this and use
#for name, date, shares, price in portfolio:
#    total += shares * price


#total = (portfolio_cost('portfolio.csv', errors='silent')) #variable total then calls function with filenme and optional argument to silence the alamrs - default set to warn
#print('Total cost:', total)



