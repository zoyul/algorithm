import sys
sys.setrecursionlimit(10**6)
def dfs(x):

    for next in graph[x]:
        if checked[next]:
            continue

        checked[next] = 1
        dfs(next)

n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

checked = [0] * (n+1)
ans = 0

for i in range(1, n+1):         # 모든 노드를 검사하면서 지나가지 않은 노드는 dfs 실행
    if checked[i]:
        continue

    ans += 1
    checked[i] = 1
    dfs(i)

print(ans)