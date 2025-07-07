import sys

input = sys.stdin.readline

word = list(map(str, input().split()))
num = int(input())
print(word[0][num - 1])
