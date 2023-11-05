#! /usr/bin/env/python3

#Lists
#ordered collection of arbitrary objects.
#Indexed by integers starting with 0
#use indexing operator to access and modify individual items of the list


names = ['Dave', 'Paula', 'Thomas', 'Lewis']
a = names[2]          #returns the 3rd item of the list
print(a)
names[2] = 'Tom'      #Changes the third itme to tom
print(a)              #variable are imutable 
a = names[2]          #lists are mutable
print(a)
print(names[2])
print(names[-1])      #Print from the back of the list.  ie the last item
print(names[-2])      #Print second to last item in list

#To append new items to a list use append() method

print(names)
names.append('Alex')     #Appends to end of list
print(names)
print(names[-1])      #Print from the back of the list.  ie the last item
names.pop()
print(names)
print(names[-1])      #Print from the back of the list.  ie the last item
names.insert(2, 'Aya')
print(names[2])
print(names)          #['Dave', 'Paula', 'Aya', 'Tom', 'Lewis']

b = names[0:2]        #b -> ['Dave','Paula']
print(b)
c = names[2:]         #c -> ['Aya','Tom', 'Lewis']
print(c)
names[1] = 'Becky'    #replaces Paula with Becky
print(names)
names[0:2] = ['Dave', 'Mark', 'Jeff']   #replaces first 2 items in list with these three 
print(names)          #['Dave', 'Mark', 'Jeff', 'Aya', 'Tom', 'Lewis']


#concatenate lists with + operator

a = ['x','y'] + ['z','z','y']
print(a)


#an empty list

names = []
print(names)

names = ['Dave', 'Paula', 'Thomas', 'Lewis']
print(names)

names = list()    #notice brackets are for list - it is the name of the class assoicated with this list type.  More common to see it used when performing coinversions of data to a list.
print(names)

#for example use list to perform data converion to characters

letters = list('Dave')
print(letters)     # ['D', 'a', 'v', 'e']

#Lists can contain different types of python objects, including other lists

d = [1, 'Dave', 3.14, ['Mark', 7, 9, [100, 101]], 10]
print(d)           #prints lists within lists just like entered above

print(d[1])        #should return second element - Dave

print(d[3][2])     #should return from list at 4th index, the 3rd elemet - ie 9

print(d[3][3][0])  #Should return from the list at 4th index, 4th index and 0 element - ie 100




