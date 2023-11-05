#! /usr/bin/env python3

# code6.py

import os

filename1 = 'data1.txt'
filename2 = 'data2.txt'

def main():
    data1 = dict()
    data2 = dict()
    breakpoint()

    with open(filename1) as file1:
        for line in file1:
            parts = line.rstrip().split(':')
            key = parts[0]
            value = parts[1]
            if key in data1:
                data1[key].append(value)
            else:
                data1[key] = [value]

    with open(filename2) as file2:
        for line in file2:
            parts = line.rstrip().split(':')
            key = parts[0]
            value = parts[1]
            if key in data2:
                data2[key].append(value)
            else:
                data2[key] = [value]

    for key in data1:
        if key in data2:
            values = (data1[key] + data2[key])
            values_str = ','.join(values)
            print(f"{key}:{values_str}")
    breakpoint()        
    return data1, data2 #returns tuple 

if __name__ == "__main__":
    result = main()
    d1 = result[0]
    d2 = result[1]


    



            
