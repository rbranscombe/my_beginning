#!/usr/bin/env python3

#code1.py

import os

filename1 = "data1.txt"
filename2 = "data2.txt"


def main():
    data1 = {}
    data2 = {}

    with open(filename1) as file1:
        for row in file1:
            #key, value = row.rstrip().split(":")
            d_parts = row.rstrip().split(":")
            d_key = d_parts[0]
            d_value = d_parts[1]
            if d_key in data1:
                data1[d_key].append(d_value)
            else:
                data1[d_key] = [d_value]

    with open(filename2) as file2:
        for row in file2:
            d_parts = row.rstrip().split(":")
            d_key = d_parts[0]
            d_value = d_parts[1]
            if d_key in data2:
                data2[d_key].append(d_value)
            else:
                data2[d_key] = [d_value]

    for d_key in data1:
        if d_key in data2:
            values = sorted(data1[d_key]) + data2[d_key]
            values_str = ",".join(values)
            print(f"{d_key}:{values_str}")

if __name__ == "__main__":
    main()
            
           
