#!/usr/bin/env python3

#Dictionary is a mapping between keys and values.  One creates a dictionary by enclosing key-value pairs

s = {'name' : 'GOOG', 'shares' : 100, 'price' : 490.10}

print("")
print(f's with original key : value mapping is {s}')

#to access members of a dictionary, use the indexing operator

name = s['name']
cost = s['shares'] * s['price']

print(f'use name key to display name value: {name}')
print(f'use math to calculate cost of shares @ shareprice: ${cost:0.2f}')


#One can insert or modify objects into a dictionary

s['shares'] = 75
print(f'S with modified shares is {s}')
s['date'] = '2007-06-07'
print(f'S with added value date is {s}')
print("")

#Dictionary is a useful way to define an object that consists of named fields.
#Dictionaries are also commonly used as a mapping for performing fast lookups on unordered data.

prices = {'GOOG' : 490.1, 'AAPL' : 125.5, 'IBM' : 91.5, 'MSFT' : 52.13}

print(f'Stock prices Dictionary Sym : Price {prices}')

p = prices['IBM']

print(f'IBM price straight from table: ${p:0.2f}')

#Use del statement to remove an element from a dictionary:

del prices['IBM']

#Dictionary membership is tested with the in operator
Method = int(input("Enter 0 or 1 for method - 1 is get(), 0 is if "))
if Method == 1:
    

     if 'IBM' in prices:
         p = prices['IBM']
     else:
         p = 0.0

     print(f'IBM price from if conditional: ${p:0.2f}')

else:

    #Use the get() method

    p = prices.get('IBM', 0.0)  #prices ['IBM'] if it exits, else 0.0

    print(f'IBM price from get() method: ${p:0.2f}')


    
    
