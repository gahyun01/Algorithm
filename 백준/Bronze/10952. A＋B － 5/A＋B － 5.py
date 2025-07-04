import sys

input = sys.stdin.readline

sum = []
while True:
    num1, num2 = map(int, input().split())
    if num1 == 0 and num2 == 0:
        break
    sum.append(num1 + num2)

i = 0
while True:
    if i == len(sum):
        break
    print(sum[i])
    i += 1
