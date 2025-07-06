N, M = map(int, input().split())

i = 0
basket = [0 for i in range(N)]
for i in range(N):
    basket[i] = i + 1

j = 0
for j in range(M):
    num1, num2 = map(int, input().split())
    basket[num1 - 1], basket[num2 - 1] = basket[num2 - 1], basket[num1 - 1]

print(*basket)