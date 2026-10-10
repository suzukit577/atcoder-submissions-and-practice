from collections import deque
from collections import defaultdict

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
connected_num = defaultdict(int)
visited = [False for _ in range(N)]
for i in range(N):
    if not visited[i]:
        queue.append(i)
        visited[i] = True
        connected_num[i] += 1
    while len(queue) != 0:
        u = queue.popleft()
        for v in graph[u]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                connected_num[i] += 1

ans = 0
for c in connected_num.values():
    ans += c * (c - 1) // 2
ans -= M
print(ans)
