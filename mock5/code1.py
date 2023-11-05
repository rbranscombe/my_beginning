#! /usr/bin/env python3

import collections

#code1.py

filename1 = "data1.txt"
filename2 = "data2.txt"

def main():
    data1 = collecitons.defaultdict(list)
    data2 = collections.defaultdict(list)

    #bring in data and condition

    with open(filename1) as file1:
        for line in file1:
            parts = line.rstrip().split(":")
            key = parts[0]
            value = parts[1]
            data1[key].append(value)


    with open(filename2) as file2:
        for line in file2:
            parts = line.rstrip().split(":")
            key = parts[0]
            value = parts[1]
            data2[key].append(value)

    
        
