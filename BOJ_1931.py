"""

최대한 많이 사용하려면?
1. 빨리 끝나는 회의부터 찾아서
2. 차례차례 회의 스케줄에 넣음

"""

N = int(input())
meeting = []
for _ in range(N):
    meeting.append(list(map(int, input().split())))

# 끝나는 시간 오름차순으로 정렬
meeting.sort(key = lambda x: (x[1], x[0]))
print(meeting)

count = 1
tmp = meeting[0][1] # 첫 회의의 끝나는 시간
for i in meeting[1:]:
    if tmp <= i[0]:
        count += 1
        tmp = i[1]

print(count)


