"""
Mr. Vincent works in a door mat manufacturing company.
One day, he designed a new door mat with the following specifications:

Mat size must be N X M. (N is an odd natural number, and M is 3 times N.)

The design should have 'WELCOME' written in the center.
"""

N,M=list(map(int,input().split()))
j=1
for i in range(N):
    if(i<N//2):
        print((".|."*j).center(M,"-"))
        j+=2
    elif(i==N//2):
        print(("WELCOME").center(M,"-"))
    elif(i>N//2):
        j -= 2
        print((".|."*j).center(M,"-"))
