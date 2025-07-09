import sys

input = sys.stdin.readline

count = int(input())

word = [[] for i in range(count)]
for i in range(count):
    a, b = map(str, input().split())
    a = int(a)
    b = list(b)
    for j in range(len(b)):
        for k in range(a):
            word[i].append(b[j])

for i in range(count):
    print(''.join(word[i]))
