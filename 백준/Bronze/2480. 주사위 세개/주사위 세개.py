num1, num2, num3 = map(int, input().split())

if num1 == num2 == num3:
  print(10000 + num1 * 1000)
elif num1 == num2 or num1 == num3:
  print(1000 + num1 * 100)
elif num2 == num3:
  print(1000 + num2 * 100)
else:
  print(max(num1, num2, num3) * 100)
