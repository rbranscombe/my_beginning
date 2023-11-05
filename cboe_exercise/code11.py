#! /usr/bin/env python3
#code11.py

import collections

filename1 = "data1.txt"
filename2 = "data2.txt"

def main():
    data1 = collections.defaultdict(list)
    data2 = collections.defaultdict(list)

    with open(filename1) as file1:
        for line in file1:
            parts = line.strip().split(":")
            key = parts[0]
            value = parts[1]
            data1[key].append(value)

    with open(filename2) as file2:
        for line in file2:
            parts = line.strip().split(":")
            key = parts[0]
            value = parts[1]
            data2[key].append(value)

    for key in data1:
        if key in data2:
            values = (
                data1[key] +
                data2[key]
            )
            str_values = ",".join(values)
            print(f"{key}:{str_values}")

if __name__ == "__main__":
    main()



