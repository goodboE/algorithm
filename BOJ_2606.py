n = int(input())
m = int(input())
matrixt = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    link = list(map(int, input().split()))
    matrixt[link[0]][link[1]] = 1
    matrixt[link[1]][link[0]] = 1

def dfs(here, graph, visited):
    visited += [here]
    for i in range(len(graph[here])):
        if graph[here][i] == 1 and (i not in visited):
            dfs(i, graph, visited)
    return len(visited)-1

print(dfs(1, matrixt, []))