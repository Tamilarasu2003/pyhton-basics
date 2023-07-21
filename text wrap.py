"""
You are given a string S and width w.

Your task is to wrap the string into a paragraph of width w.
"""

import textwrap

def wrap(string, max_width):
    result=textwrap.fill(string,width=max_width)
    return result

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)