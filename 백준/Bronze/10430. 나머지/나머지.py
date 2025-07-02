import sys

A, B, C = map(int, input().split())

sys.stdout.write(str((A + B) % C) + "\n")
sys.stdout.write(str((A % C + B % C) % C) + "\n")
sys.stdout.write(str(A * B % C) + "\n")
sys.stdout.write(str((A % C) * (B % C) % C) + "\n")