import sys
input = sys.stdin.readline

A = int(input().strip())
B = int(input().strip())

if 0 <= A:
    if 0 <= B:
        print("1")
    else:
        print("4")
else:
    if 0 <= B:
        print("2")
    else:
        print("3")