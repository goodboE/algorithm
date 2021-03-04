N, M = map(int, input().split()) # N은 박스의 개수, M은 책의 개수
box = list(map(int, input().split()))
book = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if book[j] <= box[i]:
            box[i] -= book[j]
            book[j] = 0

print(sum(box))






