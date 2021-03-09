N = int(input())
distance = list(map(int, input().split()))
price = list(map(int, input().split()))

min_price = 1000000000
result = 0

for i in range(N-1):
    tmp = price[i]
    if min_price > tmp:
        min_price = tmp
    result += distance[i] * min_price

print(result)