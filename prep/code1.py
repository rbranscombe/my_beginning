#!/usr/bin/env python

filename1 = "data1.txt"
filename2 = "data2.txt"

def main():
    data1 = {}
    data2 = {}

    with open(filename1) as file1:
        for row in file1:
            key, value = row.strip().split(":")
            data1[key] = [value]

    with open(filename2) as file2:
        for row in file2:
            key, value = row.strip().split(":")
            data2[key] = [value]

    for key in data1:
        if key in data2:
            values = data1[key] + data2[key]
            values_str = ",".join(values)
            print(f"{key}:{values_str}")

if __name__ == "__main__":
    main()
