import sys

def check(i, j):
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]

    # 공백 q 생성, 시작점 넣어주기
    q = []
    q.append((i, j))
    checked[i][j] = 1

    while q:
        now_i, now_j = q.pop(0)

        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]

            # 범위를 벗어났거나 검사할 필요가 없는 곳은 pass
            if next_i < 0 or next_j < 0 or next_i >= n or next_j >= n:
                continue
            if MAP[next_i][next_j] <= check_value:
                continue
            if checked[next_i][next_j]:
                continue

            checked[next_i][next_j] = 1
            q.append((next_i, next_j))

n = int(sys.stdin.readline())
MAP = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_value = 0
for i in range(n):
    for j in range(n):
        if MAP[i][j] > max_value:
            max_value = MAP[i][j]

ans = 0

for check_value in range(max_value+1):

    cnt = 0
    checked = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if checked[i][j]:
                continue
            if MAP[i][j] <= check_value:                  # 물에 잠기는 곳 표시
                checked[i][j] = 1
            else:                               # 물에 잠기지 않는 곳이라면 bfs 검사
                check(i, j)
                cnt += 1
    check_value -= 1

    if ans < cnt:                       # 최대값 찾기
        ans = cnt

print(ans)