import sys

input = sys.stdin.readline

max, count = map(int, input().split())

c = 0
basket = [0 for i in range(max)]
for c in range(count):
    i, j, k = map(int, input().split())
    r = 0
    for r in range(j - i + 1):
        basket[i - 1] = k
        i += 1
        r += 1

    c += 1

print(*basket)
