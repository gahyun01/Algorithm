import sys

input = sys.stdin.readline

count = int(input())
line = []
line.append(input().split())
num = int(input())

sum = 0
i = 0
for i in range(count):
    if int(line[0][i]) == num:
        sum += 1

print(sum)
