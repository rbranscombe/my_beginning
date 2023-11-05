#port4.py
#Modify file reader to be generic using Module we created called reader.py - exercise 6.2

from . import reader  #Make import package-relative

def read_portfolio(filename, *, errors='warn'):
    '''
    Read a CSV file with name, date, shares and price data into a list.
    '''
    
    return reader.read_csv(filename, [str, str, int, float], errors=errors)


if __name__ == '__main__':
    portfolio = read_portfolio('portfolio.csv')

    total = 0.0
    for items in portfolio:
        total += items['shares']*items['price']

    print('Total cost:', total)






