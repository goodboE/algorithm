import sys; sys.setrecursionlimit(10000)
from collections import deque

def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        v = queue.popleft()
        for l in range(4):
            ny = v[0] + dy[l]
            nx = v[1] + dx[l]
            if 0 <= nx < n and 0 <= ny < m and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((ny, nx))


if __name__ == '__main__':
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        graph = [[0] * n for _ in range(m)]
        cnt = 0
        for _ in range(k):
            x, y = map(int, input().split())
            graph[y][x] = 1
        for i in range(m):
            for j in range(n):
                if graph[i][j] == 1:
                    graph[i][j] = 0
                    bfs(i,j)
                    cnt += 1
        print(cnt)
