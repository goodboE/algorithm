from collections import deque

n, m, v = map(int, input().split())
matrix = [[0] * (n+1) for _ in range(n+1)]
for _ in range(m):
    link = list(map(int, input().split()))
    matrix[link[0]][link[1]] = 1
    matrix[link[1]][link[0]] = 1

def dfs(here, graph, visited ):
    visited += [here]
    for search_node in range(len(graph[here])):
        if graph[here][search_node] and search_node not in visited:
            dfs(search_node, graph, visited)
    return visited



def bfs(here, graph, visited):
    queue = deque([here])
    visited += [here]
    while queue:
        v = queue.popleft()
        for search_node in range(len(graph[here])):
            if graph[v][search_node] and search_node not in visited:
                queue.append(search_node)
                visited += [search_node]
    return visited




print(*dfs(v, matrix, []))
print(*bfs(v, matrix, []))