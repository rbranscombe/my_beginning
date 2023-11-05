#port1.py
#Modify file reader to be generic using function - exercise 4.1

import csv

def portfolio_cost(filename, *, errors='warn'):
    '''
    Computes total shares*price for a CSV file with name, date, shares and price data
    '''
    
    if errors not in { 'warn', 'silent', 'raise' }:
        raise ValueError("Errors must be one of 'warn', 'silent', 'raise'")
    
    total = 0.0

    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)           #skip a single line of input to accomodate header row
        #rowno = 1                      replace with enmumerate function
        for rowno, row in enumerate(rows, start=1): #enumerate function allows builtin counter
            #rowno += 1                 replace with enumerate function
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
                total += row[2]*row[3]     #Total shares x total price
            except ValueError as err:  #write exception ValueError reason to variable err
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row:', row)
                    print('Row:', rowno, 'Error Reason:', err)
                elif errors == 'raise':
                    raise              #reraises the last exception
                else:
                    pass               #ignore
                continue               #skips to next row
           
    return total                       #modified to return total so that it's value comes back out of private function for user to use however they want 

total = (portfolio_cost('missing.csv', errors='silent')) #variable total then calls function with filenme and optional argument to silence the alamrs - default set to warn
print('Total cost:', total)



