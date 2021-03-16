N, K = map(int, input().split())
bench = list(input())
eaten = [False] * N

for i in range(N):
    if bench[i] == 'H': continue
    for j in range(max(0, i-K), min(N, i+K+1)):
        if bench[j] == 'H' and not eaten[j]:
            break
    else:
        continue
    eaten[j] = True
print(sum(eaten))


