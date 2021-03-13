T = int(input())
for i in range(T):
    black = 0; white = 0
    n = int(input())
    first = list(input())
    second = list(input())
    for j in range(n):
        if first[j] != second[j]:
            if first[j] == 'B':
                black += 1
            else:
                white += 1
    print(max(black, white))