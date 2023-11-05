#! /usr/bin/env python3

#code1.py

filename1 = "data1.txt"
filename2 = "data2.txt"

def main():
    data1 = {}
    data2 = {}

    with open(filename1) as file1:
        for row in file1:
            dict_parts = row.rstrip().split(":")
            key = dict_parts[0]
            value = dict_parts[1]
            if key in data1:
                data1[key].append(value)
            else:
                data1[key]=[value]
            
    with open(filename2) as file2:
        for row in file2:
            dict_parts = row.rstrip().split(":")
            key = dict_parts[0]
            value = dict_parts[1]
            if key in data2:
                data2[key].append(value)
            else:
                data2[key]=[value]


    for key in data1:
        if key in data2:
            values = data1[key] + data2[key]
            values_str = ",".join(values)
            print(f"{key}:{values_str}")

if __name__ == "__main__":
    main()
            
