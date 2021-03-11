N = int(input())
point = []
for _ in range(N):
    point.append(int(input()))


point.reverse()
tmp = point[0]
count = 0
for i in point[1:]:
    if tmp <= i:
        count += i - tmp + 1
        tmp -= 1
    else:
        tmp = i

print(count)
