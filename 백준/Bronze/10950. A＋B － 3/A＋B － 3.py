count = int(input())

i = 0
sum = []
for i in range(count):
  num1, num2 = map(int, input().split())
  sum.append(int(num1 + num2))
  i += 1

j = 0
for j in range(count):
  print(sum[j])
