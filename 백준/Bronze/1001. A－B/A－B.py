import sys
input = sys.stdin.readline

A, B = map(int, input().split())
sys.stdout.write(str(A - B) + '\n')