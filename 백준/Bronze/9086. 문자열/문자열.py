import sys

input = sys.stdin.readline

test = int(input())

words = []
for i in range(test):
    word = list(input().strip())
    words.append(word)

for j in range(test):
    print(words[j][0] + words[j][-1])
