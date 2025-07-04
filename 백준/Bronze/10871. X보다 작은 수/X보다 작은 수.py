import sys

input = sys.stdin.readline

count, num = map(int, input().split())
line = list(map(int, input().split()))

i = 0
for i in range(count):
    if line[i] < num:
        print(line[i], end=' ')
        i += 1
    else:
        i += 1
