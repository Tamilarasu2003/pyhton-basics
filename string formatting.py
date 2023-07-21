"""
Given an integer, n, print the following values for each integer i from 1 to n:

Decimal
Octal
Hexadecimal (capitalized)
Binary
"""
def print_formatted(number):
    nbin = format(n,'b')
    size=len(nbin)
    for i in range(1,n+1):
        dec="{:d}".format(i)
        octa="{:o}".format(i)
        hexa="{:X}".format(i)
        bina="{:b}".format(i)
        print(str(dec).rjust(size), str(octa).rjust(size), str(hexa).rjust(size), str(bina).rjust(size))


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)