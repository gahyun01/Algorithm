import sys

input = sys.stdin.readline

count = int(input())
scores = list(map(int, input().split()))
max = max(scores)

i = 0
sum = 0
for i in range(count):
    sum = sum + scores[i] / max * 100

print(sum / count)
