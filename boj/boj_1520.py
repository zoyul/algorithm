import sys
sys.setrecursionlimit(10**6)

def dfs(now_i, now_j):

    # 끝까지 도달했다면
    if now_i == (m-1) and now_j == (n-1):
        return 1

    # dp에 기록되어 있으면
    if dp[now_i][now_j] != -1:
        return dp[now_i][now_j]

    ret = 0
    for k in range(4):
        next_i = now_i + di[k]
        next_j = now_j + dj[k]

        # 범위를 벗어면 pass
        if next_i < 0 or next_i >= m or next_j < 0 or next_j >= n:
            continue
        # 기준보다 크면 pass
        if MAP[next_i][next_j] >= MAP[now_i][now_j]:
            continue
        ret += dfs(next_i, next_j)

    dp[now_i][now_j] = ret
    return dp[now_i][now_j]

m, n = map(int, sys.stdin.readline().split())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]
print(dfs(0, 0))