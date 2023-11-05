#! /usr/bin/python3

import collections

#code1.py

#define globals

filename1 = "data1.txt"
filename2 = "data2.txt"

def main():
    data1 = collections.defaultdict(list)
    data2 = collections.defaultdict(list)

    #read in file data and condition it

    with open(filename1) as file1:
        for line in file1:
            parts = line.rstrip().rsplit(":")
            key = parts[0]
            value = parts[1]
            data1[key].append(value)

    with open(filename2) as file2:
        for line in file2:
            parts = line.rstrip().rsplit(":")
            key = parts[0]
            value = parts[1]
            data2[key].append(value)

    #find key in file1 and then check for same in file2.  If found print values in form shown

    for key in data1:
        if key in data2:
            values = data1[key] + data2[key]
            value_str = ','.join(values)
            print(f"{key}:{value_str}")

if __name__ == "__main__":
    main()
