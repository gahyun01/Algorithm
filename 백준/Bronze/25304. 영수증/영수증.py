total = int(input())
count = int(input())

i = 0
for i in range(count):
  i += 1
  price, num = map(int, input().split())
  total -= price * num

if total == 0:
  print("Yes")
else:
  print("No")
