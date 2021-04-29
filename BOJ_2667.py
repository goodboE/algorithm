n = int(input()); graph = []; result = 0; count = 0; danji = []
for i in range(n):
    graph.append(list(map(int, input())))

def dfs(x, y):
    global count
    if x <= -1 or x >= n or y >= n or y <= -1:
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            result += 1
            danji.append(count)
            count = 0

danji.sort()
print(result)
for k in danji:
    print(k)
