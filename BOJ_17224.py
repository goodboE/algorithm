N, L, K = map(int, input().split())
easy, hard = 0, 0

for _ in range(N):
    sub1, sub2 = map(int, input().split())
    if sub2 <= L:
        hard += 1
    elif sub1 <= L:
        easy += 1

score = 140 * min(hard, K)
if hard < K:
    score += 100 * min(K-hard, easy)

print(score)

