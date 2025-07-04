import sys

input = sys.stdin.readline

result = []
while True:
    line = input()
    if not line:
        break
    try:
        num1, num2 = map(int, line.split())
        result.append(num1 + num2)
    except:
        break

for r in result:
    print(r)
