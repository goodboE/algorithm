n = int(input())
iron_rod = sorted(list(map(int, input().split())))
sum_iron_rod = sum(iron_rod)
count = 0

for i in iron_rod:
    sum_iron_rod -= i
    count += i * sum_iron_rod

print(count)
