n = int(input()) # 좌석의 수
seats = input()
count = 0
# LL을 한좌석으로 생각하면(C) 컵홀더의 개수 = 좌석개수 + 1
seat = seats.replace('LL', 'C')
# 컵 홀더의 개수가 사람 수보다 많을수도 있음!!
print(min(len(seat) + 1, n))