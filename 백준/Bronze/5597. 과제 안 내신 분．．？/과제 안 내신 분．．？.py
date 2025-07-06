import sys

input = sys.stdin.readline

data = [int(input()) for _ in range(28)]
check_list = range(1, 31)

for i in check_list:
    if i not in data:
        print(i)
