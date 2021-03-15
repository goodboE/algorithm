N = int(input())
withdraw_time = sorted(list(map(int, input().split())))

tmp = 0; sum = 0
for i in range(N):
    tmp += withdraw_time[i]
    sum += tmp

print(sum)