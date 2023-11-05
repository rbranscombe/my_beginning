#!/usr/bin/env python3

#interest.py

principal = 1000               #Initial amount
rate = 0.05                    #Interest rate
numyears = 5                   #number of years
year = 1
base_year = 2020
while year <= numyears:
    principal = principal * (1 + rate)
    #print(year, principal)
    #print(f'{year:>3d} {principal:0.2f}') #>3d means 3-digit decimal number right aligned
                                          #0.2f means a floating point number with 2 decimal places of accuracy

    #modify the code to show f escaped expressions within a string on a more complex string
    #print(f'{base_year + year:>4d} {principal:0.2f}')

    #As an alternative to f-strings, the format() method and % operator are also sometimes used to format strings

    print('{0:>3d}  {1:0.2f}'.format(year, principal))
    print('%3d %0.2f'  %  (year, principal))
    
    year += 1


