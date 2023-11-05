#! usr/bin/env/ python3

#pcost.py
#
#Reads input lines of the form 'NAMES,SHARES,PRICE'.
#For example:
#
#SYM,123,456.78
#
import sys                   #import statement to load the sys module from python library
print("This is the name of the script: ", sys.argv[0])
print("Number of arguments: ",len(sys.argv))
print("The arguemts are: ", str(sys.argv))

if len(sys.argv) != 1:       #Module is used to obtain command-line arguments found in 
    raise SystemExit(f'Usage: {sys.argv[0]} listcomp.txt')   #list sys.argv
                             #if statement does initial check to make sure that a filename
                             #is provided.  If not a system-exit exception is raised.
                             #with a helpful error message.  I this message, sys.argv[0]
                             #inserts the name of the program that is running.
rows = []
with open(sys.argv[0], 'rt') as file:   #The open() function uses the filename that 
    for line in file:                   #was specified on the command line.
       rows.append(line.split(','))    #the for lin in file loop is reading the file line by
                                        #line.  Each line is split into a small list
                                        #using the comma as delimiter. List is appended to
                                        #rows.  The final result, rows is a lis of lists
#rows is a list of this form
#[
#  ['SYM', '123', '456.78']
#  ...
#]


#List comprehension - useful technique to construct a new list by performing simple calculations all in one line of code
total = [int(row[1]) * int(row[1]) for row in rows ]  #The expression constructs a
                                                             #new list by looping all of the
                                                             #lists in rows and computing
                                                             #The product of the second and
                                                             #third items.
print(f'Total Cost: {total:0.2f}')

