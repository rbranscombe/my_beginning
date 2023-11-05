filename1 = "data1.txt"
filename2 = "data2.txt"


def main():
    data1 = {}
    data2 = {}
    with open(filename1) as file1:
        for line in file1:
            line = line.rstrip()
            key, val = line.split(':')
            data1[key] = val
    with open(filename2) as file2:
        for line in file2:
            line = line.rstrip()
            key, val = line.split(':')
            data2[key] = val
    for key,val in data1.items():
        if key in data2:
            print(f"{key}:{val},{data2[key]}")

if __name__ == "__main__":
    main()
