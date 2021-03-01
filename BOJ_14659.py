# PyPy3
n = int(input())
height = list(map(int, input().split()))

max_kill = 0
for i in range(n):
    prev_height = height[i]
    kill = 0
    for j in range(i+1, n):
        if prev_height > height[j]:
            kill += 1
        else:
            break
    max_kill = max(max_kill, kill)
print(max_kill)

# 더 효율적으로 짤 수 있을듯