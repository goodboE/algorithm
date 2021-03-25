"""
동전 개수가 최소가 되려면?
1. A(i)는 A(i-1)의 배수이므로 가능한 단위가 큰 동전을 많이 사용해야 한다.
"""
n, k = map(int, input().split())
coins = []; coin_count = 0

for _ in range(n):
    coins.append(int(input()))
coins.reverse()

for i, coin in enumerate(coins,1):
    if k == 0:
        break
    if k // coin >= 1:
        coin_count += k // coin
        k -= coin * (k//coin)

print(coin_count)