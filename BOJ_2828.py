N, M = map(int, input().split()) # N: 스크린, M: 바구니
apple = int(input()) # 사과의 개수
move = 0 # 이동 횟수
position_M = [i for i in range(1, M+1)] # 바구니의 위치

for i in range(apple):
    k = int(input())
    if max(position_M) < k:
        move += k - max(position_M)
        position_M = [j for j in range(k, k-M, -1)]
    elif min(position_M) > k:
        move += min(position_M) - k
        position_M = [l for l in range(k, k+M)]

print(move)








