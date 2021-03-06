# 1이나 0에서 0이나 1로 바뀔때마다 count+1
# count = 0 이면 행동횟수 0
# -----------------------
# count = 1 이면 행동횟수 1
# count = 2 이면 행동횟수 1
# count = 3 이면 행동횟수 2
# count = 4 이면 행동횟수 2
# count = 5 이면 행동횟수 3
# ,,,,

S = input()
count = 0 # 행동 횟수
prev_s = S[0]

for i in range(1, len(S)):
    if prev_s != S[i]:
        count += 1
        prev_s = S[i]
    else:
        pass

if count == 0:
    print(0)
elif count % 2 != 0:
    print(count//2 + 1)
else:
    print(count//2)

