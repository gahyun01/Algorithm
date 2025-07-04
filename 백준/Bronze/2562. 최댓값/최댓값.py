import sys

input = sys.stdin.readline

i = 0
max = -1
line = 0
for i in range(9):
    a = int(input())
    if a > max:
        max = a
        line = i + 1

print(max)
print(line)
