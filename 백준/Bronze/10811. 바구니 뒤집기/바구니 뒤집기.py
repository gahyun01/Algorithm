import sys

input = sys.stdin.readline

num, count = map(int, input().split())
basket = list(range(1, num + 1))

i = 0
for i in range(count):
    a, b = map(int, input().split())
    basket[a - 1:b] = basket[a - 1:b][::-1]

print(*basket)
