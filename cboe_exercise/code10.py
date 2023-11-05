#! usr/shared/env/ python3

#code10.py

import os

import collections

#assign globals
filename1 = "data1.txt"
filename2 = "data2.txt"

def main():
    data1 = collections.defaultdict(list)
    data2 = collections.defaultdict(list)

    #condition file data
    with open(filename1) as f1:
        for ln in f1:
            d_parts = ln.rstrip().split(":")
            d_key = d_parts[0]
            d_value = d_parts[1]
            data1[d_key].append(d_value)

    with open(filename2) as f2:
        for ln in f2:
            d_parts = ln.rstrip().split(":")
            d_key = d_parts[0]
            d_value = d_parts[1]
            data2[d_key].append(d_value)

    #iteratre over data1 dict key and look for same in data2.  When same key found, print key and all associated values
    for d_key in data1:
        if d_key in data2:
            values =(
                data1[d_key]+
                data2[d_key]
            )    
            str_values = ','.join(values)
            print(f"{d_key}:{str_values}")
    return data1, data2

if __name__ == "__main__":
    result = main()
    d1 = result[0]
    d2 = result[1]
