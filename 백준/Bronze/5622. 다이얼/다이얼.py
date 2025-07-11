import sys
import re

input = sys.stdin.readline

num_list = {
    'ABC': 3,
    'DEF': 4,
    'GHI': 5,
    'JKL': 6,
    'MNO': 7,
    'PQRS': 8,
    'TUV': 9,
    'WXYZ': 10
}

word = list(input().strip())

seconds = 0
for w in word:
    for num in num_list:
        if w in num:
            seconds += num_list[num]

print(seconds)
