hour, minute = map(int, input().split())

if minute < 45:
    minute = minute - 45
    minute = 60 + minute
    if hour == 00:
        hour = 23
        print(f"{hour} {minute}")
    else:
        hour -= 1
        print(f"{hour} {minute}")

else:
    minute = minute - 45
    print(f"{hour} {minute}")
