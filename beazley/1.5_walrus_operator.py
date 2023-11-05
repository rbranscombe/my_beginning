#! /usr/bin/env/python 3

# example of assignment expression - walrus operator
# assignment of a variable and a conditional combined together using the := operator.
# added break and continue statements to the code to test.  original walrus operator is without them

#parenthesis used to surround an assignment expression are always required.

x = 0
while (x := x + 1) < 10: #prints
    if x == 5:
        #break # Stops the loop. moves to done below
        continue #skips the print(x) and continues the loop
    print(x)

print('done')
print('''Content-type: text/html

<h1> Hello Wolrd </h1>
Click <a href="http://www.python.org"

''') # demonstrates the use of the triple quote for multiple line 

    
