import sys

input = sys.stdin.readline

count = int(input())
nums = list(str(input().strip()))
nums = [int(i) for i in nums]
print(sum(nums))
