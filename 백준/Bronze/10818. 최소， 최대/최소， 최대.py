import sys

input = sys.stdin.readline

count = int(input())
num = list(map(int, input().split()))

i = 0
max = -1000000
min = 1000000
for i in range(count):
    if num[i] > max:
        max = num[i]
    if num[i] < min:
        min = num[i]

print(f"{min} {max}")
