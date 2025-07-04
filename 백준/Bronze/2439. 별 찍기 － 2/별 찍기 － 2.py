import sys

input = sys.stdin.readline

count = int(input())

i = 0
for i in range(count):
    print(" " * (count - i - 1) + "*" * (i + 1))
