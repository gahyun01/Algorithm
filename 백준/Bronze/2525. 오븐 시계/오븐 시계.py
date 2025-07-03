hour, minute = map(int, input().split())
m = int(input())

minute = minute + m

if minute >= 60:
    hour += minute // 60
    minute = minute % 60

if hour >= 24:
    hour = hour % 24
print(f"{hour} {minute}")
