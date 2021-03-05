# 연속하는 P일 중, L일 사용 가능, 총 V일짜리 휴가
# V//P * L + V%P == 최대 사용
# 예외 : V%P가 L보다 큰 경우가 있는데 이럴때는 L을 더해줘야 함
can_camping = []

while True:
    L, P, V = map(int, input().split())
    if (L == 0 and P == 0 and V == 0):
        break
    else:
        can_camping.append((V//P * L) + min(V%P, L))

for i, v in enumerate(can_camping):
    print('Case %d: %d' %(i+1, v))