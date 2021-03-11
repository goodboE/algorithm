from collections import Counter

N = int(input())
ddeokguk = [i for i in map(int, input().split())]
print(max(Counter(ddeokguk).values()))