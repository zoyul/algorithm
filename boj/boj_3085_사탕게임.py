"""
1번째 방법

import sys
from collections import deque

# 가장 긴 행 계산
def check_left(now_i, now_j):

    max_cnt = 1

    for i in range(now_i, now_i+2):
        if i >= n:
            break
        visited = [0] * n
        for j in range(n):
            # 방문한 곳은 무시
            if visited[j]:
                continue

            visited[j] = 1

            q = deque()
            q.append((i, j))
            cnt = 0

            while q:
                now_i, now_j = q.popleft()
                cnt += 1

                next_i = now_i
                next_j = now_j + 1

                # 범위를 벗어나거나 다른 사탕이면 무시
                if next_j >= n:
                    continue
                if MAP[now_i][now_j] != MAP[next_i][next_j]:
                    continue

                visited[next_j] = 1
                q.append((next_i, next_j))

            max_cnt = max(max_cnt, cnt)
    return max_cnt

# 가장 긴 열 계산
def check_down(now_i, now_j):

    max_cnt = 1

    for j in range(now_j, now_j+2):
        if j >= n:
            break
        visited = [0] * n
        for i in range(n):
            # 방문한 곳은 무시
            if visited[i]:
                continue

            visited[i] = 1

            q = deque()
            q.append((i, j))
            cnt = 0

            while q:
                now_i, now_j = q.popleft()
                cnt += 1

                next_i = now_i + 1
                next_j = now_j

                # 범위를 벗어나거나 다른 사탕이면 무시
                if next_i >= n:
                    continue
                if MAP[now_i][now_j] != MAP[next_i][next_j]:
                    continue

                q.append((next_i, next_j))

            max_cnt = max(max_cnt, cnt)
    return max_cnt

# 근접한 캔디가 다르면 바꾸는 함수
def change(now_i, now_j):
    max_cnt = 1

    for k in range(2):
        change_i = now_i + di[k]
        change_j = now_j + dj[k]

        # 범위 벗어나거나 똑같은 사탕이면 무시
        if change_i >= n or change_j >= n:
            continue
        if MAP[change_i][change_j] == MAP[now_i][now_j]:
            continue

        # 사탕 바꾸기
        candy = MAP[now_i][now_j]
        change_candy = MAP[change_i][change_j]

        MAP[now_i][now_j] = change_candy
        MAP[change_i][change_j] = candy

        # 최대값 구하기
        max_cnt = max(max_cnt, check_left(now_i, now_j), check_down(now_i, now_j))

        # 원상복구
        MAP[now_i][now_j] = candy
        MAP[change_i][change_j] = change_candy

    return max_cnt

n = int(sys.stdin.readline())
MAP = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

di = [0, 1]
dj = [1, 0]

ans = 1
for i in range(n):
    ans = max(ans, check_left(i, 0), check_down(i, 0))
    for j in range(n):
        ans = max(ans, change(i, j))

print(ans)

# https://www.acmicpc.net/board/view/58247 반례모음

"""
import sys
from collections import deque

# 가장 긴 행 계산
def check_left(now_i, now_j):

    if now_i >= n or now_j >= n:
        return 0

    max_cnt = 1

    visited = [0] * n
    i = now_i
    for j in range(n):
        # 방문한 곳은 무시
        if visited[j]:
            continue

        visited[j] = 1

        q = deque()
        q.append((i, j))
        cnt = 0

        while q:
            now_i, now_j = q.popleft()
            cnt += 1

            next_i = now_i
            next_j = now_j + 1

            # 범위를 벗어나거나 다른 사탕이면 무시
            if next_j >= n:
                continue
            if MAP[now_i][now_j] != MAP[next_i][next_j]:
                continue

            visited[next_j] = 1
            q.append((next_i, next_j))

        max_cnt = max(max_cnt, cnt)

    return max_cnt

# 가장 긴 열 계산
def check_down(now_i, now_j):

    if now_i >= n or now_j >= n:
        return 0

    max_cnt = 1

    visited = [0] * n
    j = now_j
    for i in range(n):
        # 방문한 곳은 무시
        if visited[i]:
            continue

        visited[i] = 1

        q = deque()
        q.append((i, j))
        cnt = 0

        while q:
            now_i, now_j = q.popleft()
            cnt += 1

            next_i = now_i + 1
            next_j = now_j

            # 범위를 벗어나거나 다른 사탕이면 무시
            if next_i >= n:
                continue
            if MAP[now_i][now_j] != MAP[next_i][next_j]:
                continue

            visited[next_i] = 1
            q.append((next_i, next_j))

        max_cnt = max(max_cnt, cnt)

    return max_cnt

# 근접한 캔디가 다르면 바꾸는 함수
def change(now_i, now_j):

    max_cnt = 1
    cnt_left, cnt_down = 1, 1

    for k in range(2):
        change_i = now_i + di[k]
        change_j = now_j + dj[k]

        # 범위 벗어나거나 똑같은 사탕이면 무시
        if change_i >= n or change_j >= n:
            continue
        if MAP[change_i][change_j] == MAP[now_i][now_j]:
            continue

        # 사탕 바꾸기
        candy = MAP[now_i][now_j]
        change_candy = MAP[change_i][change_j]

        MAP[now_i][now_j] = change_candy
        MAP[change_i][change_j] = candy

        if k == 0:      # 가로로 바꾸면
            cnt_left = max(check_left(now_i, now_j), check_down(now_i, now_j), check_down(now_i, now_j+1))
        elif k == 1:        # 세로로 바꾸면
            cnt_down = max(check_down(now_i, now_j), check_left(now_i, now_j), check_left(now_i+1, now_j))
        # 최대값 구하기
        max_cnt = max(max_cnt, cnt_left, cnt_down)

        # 원상복구
        MAP[now_i][now_j] = candy
        MAP[change_i][change_j] = change_candy

    return max_cnt

n = int(sys.stdin.readline())
MAP = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

di = [0, 1]
dj = [1, 0]

ans = 1
for i in range(n):
    ans = max(ans, check_left(i, 0), check_down(i, 0))
    for j in range(n):
        ans = max(ans, change(i, j))

print(ans)