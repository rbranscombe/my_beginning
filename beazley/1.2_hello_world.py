#! /usr/bin/env/python3

#illustrating unicode characters that make up strings and are referenced by the length of the string s using len(s).
#show extraction of single charachter from strin using indexing operation s[i] - i is index.and reference starts from zero.
#to extract a substring, use the slicing operator s[i:j] extracts all characters from s whose index k is in the range i<=k<j.  if either index is omited the begining and or end of string is assumed



a = 'Hello World'
print(len(a))             #11
b = a[4]                  #b = 'o'
print(b)
c = a[-1]                 #c = 'd'
print(c)

d = a[:5]                 #d = 'Hello'
print(d)
e = a[6:]                 #e = 'World'
print(e)
f = a[3:8]                #f = 'lo Wo'
print(f)
g = a[-5:]                #g = 'World'
print(g)

h = a.replace('Hello', 'Hello Cruel')   #show replace() method
print(h)                                #notice a remains the unchanged
print(a)

i = a + 'ly'                           #strings are concactenated with +
print(i)

x = '37'
y = '42'
z = x + y
print(z)                             #x and y and z are strings here z = 3742

#to make z and integer
z = int(x) + int(y)                  #z = 79
print(z)

#use str(), repr() or format() functions to creat strings from non-strings

q = 'hello\nworld'
t = 4.3598
r = 'The value of q is '
s = r + str(q)      # str() non-string converted to string hello <return> world
print(s)
s = r + repr(q)     # repr() non-string converted to string produces output as program. ie shows new line character and other for use in debugging
print(s)
s = r + format(t, '0.2f') #format() function used to convert non-string to string. 
print(s)
print(f'{t:0.2f}') #This works great as well


