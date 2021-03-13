n = int(input())
team = list(map(int, input().split()))
team.sort()
power = []

for i in range(len(team)//2):
    power.append(team[i]+team[len(team)-1-i])

print(min(power))