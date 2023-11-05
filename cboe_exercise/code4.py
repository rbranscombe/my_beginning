#!/usr/bin/env python3

import collections


filename1 = 'data1.txt'
filename2 = 'data2.txt'


def get_data_from_file(path):
    data = collections.defaultdict(list)
    with open(path) as file:
        for line in file:
            parts = line.rstrip().split(':')
            key = parts[0]
            value = parts[1]
            data[key].append(value)
    return data


def main():
    data1 = get_data_from_file(filename1)
    data2 = get_data_from_file(filename2)
    for key in data1:
        if key in data2:
            values = data1[key] + data2[key]
            values_str = ','.join(values)
            print(f"{key}:{values_str}")    


if __name__ == "__main__":
    main()
