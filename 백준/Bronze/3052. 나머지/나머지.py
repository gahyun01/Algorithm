import sys

input = sys.stdin.readline

nums = [int(input()) for _ in range(10)]

remainders = []
for i in range(10):
    if nums[i] % 42 not in remainders:
        remainders.append(nums[i] % 42)

print(len(remainders))
