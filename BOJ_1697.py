from collections import deque

n, k = map(int, input().split())
visited = [0] * 100001


def bfs(x, y):
    global depth
    queue = deque()
    queue.append([x, 0])
    while queue:
        where, depth = queue[0][0], queue[0][1]
        if where == y:
            break
        queue.popleft()
        visited[where] = True
        if where - 1 >= 0 and where-1 <= 100000 and visited[where - 1] == 0:
            queue.append([where - 1, depth + 1])
        if where + 1 >= 0 and where+1 <= 100000 and visited[where + 1] == 0:
            queue.append([where + 1, depth + 1])
        if where * 2 >= 0 and where*2 <= 100000 and visited[where * 2] == 0:
            queue.append([where * 2, depth + 1])

    return queue[0][1]


print(bfs(n, k))
