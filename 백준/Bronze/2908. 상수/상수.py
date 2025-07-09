import sys

input = sys.stdin.readline

num1, num2 = list(input().split())
num1 = [int(i) for i in num1]
num2 = [int(i) for i in num2]

num1[0], num1[2] = num1[2], num1[0]
num2[0], num2[2] = num2[2], num2[0]

if num1 > num2:
    print(''.join(map(str, num1)))
else:
    print(''.join(map(str, num2)))
