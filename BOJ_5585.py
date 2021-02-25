n = int(input())
# 2839번과 달리500이 각각 100, 50, 10, 5, 1의 배수이므로
# 거스름돈 개수를 최소화 하려면 500 > 100 > 50 > 10 > 5 > 1 순서로 거슬러주면 된다.
jandon = 1000 - n
count = 0
array = [500, 100, 50, 10, 5, 1]

for coin in array:
    count += jandon // coin
    jandon %= coin
print(count)

