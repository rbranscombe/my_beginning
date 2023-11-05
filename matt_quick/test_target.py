#!/usr/bin/env python

greeting = "hello universe"


def print_greeting_target(greeting):
    if "world" in greeting:
        print("world target")
    elif "universe" in greeting:
        print("universe target")
    else:
        print("unknown target")


print_greeting_target(greeting)
