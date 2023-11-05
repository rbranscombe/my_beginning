#!/usr/bin/env python3

import os

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
    breakpoint()

def get_common_data(data1, data2):
    retdata = collections.defaultdict(list)
    for key in data1:
        if key in data2:
            retdata = data1[key] + data2[key]
    return retdata
    breakpoint()


def display_common_data(common_data):
    for key, values in sorted(common_data[0], common_data[1]):
        print(f"{key}:{','.join(values)}")



def main():
    data1 = get_data_from_file(filename1)
    data2 = get_data_from_file(filename2)
    common_data = get_common_data(data1=data1, data2=data2)
    display_common_data(common_data)


if __name__ == "__main__":
    main()
