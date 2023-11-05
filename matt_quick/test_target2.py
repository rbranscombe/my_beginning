#!/usr/bin/env python

greeting = "hello universe"


def get_greeting_target(greeting):
    if "world" in greeting:
        return "world"
    elif "universe" in greeting:
        return "universe"
    else:
        return "unknown"


my_target = get_greeting_target(greeting)
print(my_target)
