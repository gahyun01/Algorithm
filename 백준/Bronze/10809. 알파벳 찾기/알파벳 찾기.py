import sys

input = sys.stdin.readline

alist = [chr(i) for i in range(97, 123)]
word = list(input().strip())

for i in range(len(alist)):
    if alist[i] not in word:
        alist[i] = "-1"
    else:
        alist[i] = str(word.index(alist[i]))

print(*alist)
