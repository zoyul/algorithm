import sys
from collections import deque

def bfs(now_i, now_j, cnt):

    q = deque()
    q.append((now_i, now_j, cnt))

    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    while q:
        now = q.popleft()
        now_i = now[0]
        now_j = now[1]
        now_cnt = now[2]

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 지나갈 수 없는 곳이면 pass
            if next_i < 0 or next_i >= n or next_j < 0 or next_j >= m:
                continue
            if MAP[next_i][next_j] != 'L':
                continue
            if visited[next_i][next_j]:
                continue

            visited[next_i][next_j] = 1
            q.append((next_i, next_j, now_cnt + 1))

    return now_cnt

n, m = map(int, sys.stdin.readline().split())
MAP = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(m):
        if MAP[i][j] == 'L':                # 육지일 경우에 bfs 실행
            visited = [[0] * m for _ in range(n)]
            visited[i][j] = 1
            cnt = 0
            ans = max(ans, bfs(i, j, cnt))      # 각각의 최단거리 중 가장 먼 곳 찾기

print(ans)