n = int(input())
# 5가 3의 배수가 아니므로 시작부터 5kg 봉지를 무조건 많이 사용할 수 없음
bongji = 0

while n >= 0:
    if n % 5 == 0:
        bongji += n // 5
        print(bongji)
        break
    n -= 3
    bongji += 1
else:
    print(-1)
