N, L = map(int, input().split())
fruit_height = list(map(int, input().split()))
fruit_height.sort() # 앞에있는것부터 먹을 필요 없음
for i in range(N):
    if L >= fruit_height[i]:
        L += 1
print(L)





