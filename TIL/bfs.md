## :bookmark_tabs: BFS (Breadth First Search) _ 너비 우선 탐색



```python
T = 10
for tc in range(T):
    n = int(input())
    MAP = [list(map(int, input())) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]

    for i in range(16):
        for j in range(16):
            if MAP[i][j] == 3:
                goal_i = i
                goal_j = j

    now_i = 1
    now_j = 1

    q = []          # q 생성
    q.append([now_i, now_j])
    visited[now_i][now_j] = 1           # enque, 방문표시

    while len(q):
        now = q.pop(0)
        now_i = now[0]
        now_j = now[1]

        di = [0, 0, 1, -1]
        dj = [1, -1, 0, 0]
        for k in range(4):
            next_i = now_i + di[k]
            next_j = now_j + dj[k]
			
            # MAP 을 벗어나거나, 벽이거나, 지나간 흔적이 있으면 무시
            if next_i < 0 or next_i >= len(MAP) or next_j < 0 or next_j >= len(MAP):
                continue
            if MAP[next_i][next_j] == 1:
                continue
            if visited[next_i][next_j] == 1:
                continue

            q.append([next_i, next_j])
            visited[next_i][next_j] = 1

    if visited[goal_i][goal_j] == 1:
        print(f'#{n} 1')
    else:
        print(f'#{n} 0')
```

##### :star2:  bfs 는 이 틀에서 크게 벗어나지 않는다



1. ##### 연결 구조 구성
2. ##### q 생성
3. ##### 시작점 세팅( 시작점을 q에 저장)
4. ##### q 앞에서 점을 거냄
5. ##### now 에서 갈 수 있는 모든 점을 찾기
