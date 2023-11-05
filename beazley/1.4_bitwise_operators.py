#! /usr/bin/env/python3

# Bitwise Operators examples

a = 0b11001001   #decimal 201 or hex 0xc9
mask = 0b11110000

x = (a & mask) >>4     #x = 0b1100 (12)
print (x)
