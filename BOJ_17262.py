# N명의 팬들이 머무르는 시간 [s, e]
N = int(input())
fan_time = []

for _ in range(N):
    s, e = list(map(int, input().split()))
    fan_time.append([s, e])
# 가장 빨리 하교(end) ~ 가장 늦게 등교(start)
# end > start 일 경우 0
end = 100001
start = 0
for i in range(N):
    if fan_time[i][1] < end:
        end = fan_time[i][1]
    if fan_time[i][0] > start:
        start = fan_time[i][0]

if end > start:
    print(0)

else:
    print(start-end)



