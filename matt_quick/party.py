#!/usr/bin/env python3

import math


PACK_SIZE = {
    "buns": 8,
    "dogs": 10,
    "crisps": 32,
    "drinks": 6,
}


def main():
    guest_count = int(input("guests: "))
    items = PACK_SIZE.keys()
    for item in items:
        print_shopping_list_for_item(item, guest_count)


def print_shopping_list_for_item(item, guest_count):
    """\
    Print number of packs required for given item and guest_count.

    Ruth is cool.

    """
    pack_count = math.ceil(guest_count / PACK_SIZE[item])
    print(f"packs of {item}: {pack_count}")


if __name__ == "__main__":
    main()

