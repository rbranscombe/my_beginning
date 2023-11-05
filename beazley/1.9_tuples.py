#! /usr/bin/env/ python3

#Tuples are made of immutable values that cannot be changed after creation.
#Lists are mutable collections of disticnt objects that can be changed after creation

holding = ('GOOG', 100, 490.10)
address = ('www.python.org', 80)

# For completeness, 0 and 1 element tuples can be defined but have special syntax:

#a = ()            #0-tuple (empty tuple)
#b = (item,)       #1-tuple (note the trailing comma)

#values in a tuple can be extracted by numerical index just like a list.  However, it is more common to unpack tuples into a set of variables:

name, shares, price = holding
host, port = address

print(f'holding: {holding}')
print(f'name: {name}, shares: {shares}, price: {price}')

print(f'address: {address}')
print(f'host: {host}, port: {port}')

c = holding[0:2]  # tuples support slicing
print(c)
d = address[-1]
print(d)
print(address[-1])

#Tuples and lists are often used together to represent data.



