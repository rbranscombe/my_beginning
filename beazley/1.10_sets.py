#!/usr/bin/env python3

#1.10 Sets
#sets are ordered collecitons of unique objects that are used to find distinct values or memberships.
#make sets by enclusing a collecion of values in curly braces {} or give an existing collection of items to set().
#elements of a set are typically restricted to immutable objects.   set of numbers, strings or tuples.  you cannot make a set containing lists.
#when in doubt try it!
# sets are not ordered and elements can't be duplicated.


names1 = {'IBM', 'MSFT', 'AA'}
names2 = set(['IBM', 'MSFT', 'HPE', 'IBM', 'CAT'])


print(names1)
print(names2)

t = names1
s = names2
print(f't = {t}')
print(f's = {s}')

#notice that if you run the code a couple of times
#1.  the order of the printed elements is different
#2.  only 1 instance of IBM appears in name2


#list comprehension - example in 1.9_tuples3.py
#create empy set r=set()
#set supports standard collection of operations including union, interscion, difference and symmetric difference.

a = t | s            #Union {'MSFT', 'CAT', 'HPE', 'AA', 'IBM'}
print(f'union a of t |s is {a}')
b = t & s            #intersection {'IBM', 'MSFT'}
print(f'intersection b of t & s is {b}')
c = t - s            #Difference ie items in t that are not in s {'AA'}
print(f'c difference of t - s is {c}')
d = s - t            #Difference ie items in s that are not in t {'CAT', 'HPE'}
print(f'd difference of s - t is {d}')
e = t ^ s            #Symmetric difference  ie items that are in either s or t, but not in both {'CAT', 'HPE', 'AA'}
print(f'e symmetric difference t ^ s is {e}')


#new items can be added to a set using add() or update()

t.add('DIS')                       #add a single item
s.update({'JJ', 'GE', 'ACME'})     #Adds multiple items

print("""use .add() to add single item 'DIS' to t: """)
print(f't: {t}')
print("""use .update({}) to add multiple items {'JJ', 'GE', ACME'} to s: """)
print(f's: {s}')

# remove items from set with remove() or discard() - remove() has an exception if item doesnt exist.  discard() doesn't

t.remove('IBM')
s.discard('SCOX')

print(f'use remove() with exception if item doesnt exist t is equal to {t} without IBM')
print(f'use discard() with no exception if item doesnt exist s is equal to {s} - no exception raised when SCOX doesnot exist')
