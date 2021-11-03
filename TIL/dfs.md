## :bookmark_tabs: DFS (Depth First Search) _ 깊이 우선 탐색



##### 	비선형구조인 그래프 구조는 그래프로 구현된 모든 자료를 빠짐없이 검색하는 것이 중요함

​	시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법

 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 깊이 우선 탐색을 반복해야 하므로 후입선출 구조인 스택을 사용



##### 1. 배열 visitied를 0으로 초기화하고, 공백 스택을 생성

##### 2. 방문하는 정점을 stack에 push, 인접정점을 우선순위에 따라 차례대로 탐색

##### 3. 탐색하는 정점을 stack에 push, 더 이상 탐색할 곳이 없으면 pop

##### 4. pop한 곳을 기준으로 인접정점이 더 있는지 확인

##### 5. 갈 곳이 있으면 push, 갈 곳이 없으면 pop해서 다시 확인 이 작업을 반복. stack이 0이 될 때까지

##### 6. 스택이 0이 되면 탐색 종료





##### :pencil2: 기본 dfs

``` python
node = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G']
#          A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0],    # A
       [0, 1, 0, 0, 1, 1, 0, 0],    # B
       [0, 1, 0, 0, 0, 1, 0, 0],    # C
       [0, 0, 1, 0, 0, 0, 1, 0],    # D
       [0, 0, 1, 1, 0, 0, 1, 0],    # E
       [0, 0, 0, 0, 1, 1, 0, 1],    # F
       [0, 0, 0, 0, 0, 0, 1, 0]]    # G

def dfs(s, V):
    visited = [0] * (V+1)
    stack = []
    now = s
    visited[now] = 1
    print(node[now])

    while now != 0:
        for w in range(V+1):
            if adj[now][w] == 1 and visited[w] == 0:        # 인접했고, 방문x정점이면
                print(node[w])
                stack.append(w)
                now = w
                visited[w] = 1
                break
        else:                   # 다음 정점이 없으면
            if stack:
                now = stack.pop()
            else:
                now = 0
                break
    return

dfs(1, 7)

# 출력
A
B
D
F
E
C
G
```

```python
T = 10
for tc in range(T):
    t, n = map(int, input().split())
    pairs = list(map(int, input().split()))

    MAP = [[] for _ in range(100)]
    visited = [0] * 100
    for i in range(len(pairs))[::2]:
        MAP[pairs[i]].append(pairs[i+1])

    s, g = 0, 99

    stack = []
    stack.append(s)

    while stack:
        now = stack.pop()

        if now == g:
            visited[g] = 1
            break

        if visited[now]:        # 방문했다면
            continue
        visited[now] = 1

        for next in MAP[now]:
            if not visited[next]:
                stack.append(next)


    print(f'#{tc+1} {visited[99]}')
    # print(visited)
    # print(MAP)
```







##### :pencil2: dfs 재귀

```python
def dfs(now):
    for next in range(V + 1):
        if adj[now][next] == 1 and visited[next] == 0:
            visited[next] = 1
            dfs(next)


T = int(input())
for tc in range(T):
    V, E = map(int, input().split())
    adj = [[0] * (V + 1) for _ in range(V + 1)]
    visited = [0] * (V + 1)

    for i in range(E):
        nd1, nd2 = map(int, input().split())
        adj[nd1][nd2] = 1
    start, end = map(int, input().split())

    visited[start] = 1
    dfs(start)

    print(f'#{tc+1} {visited[end]}')
```





##### :pencil2: 2차원 배열

```python
def dfs(now_i, now_j):
    if now_i == goal_i and now_j == goal_j:
        return

    for k in range(4):
        next_i = now_i + di[k]
        next_j = now_j + dj[k]

        if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
            continue
        if MAP[next_i][next_j] == 1:
            continue
        if visited[next_i][next_j] != 0:
            continue

        visited[next_i][next_j] = 1
        dfs(next_i, next_j)

T = int(input())
for tc in range(T):
    n = int(input())
    MAP = [list(map(int, input())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if MAP[i][j] == 2:
                now_i = i
                now_j = j

    for i in range(n):
        for j in range(n):
            if MAP[i][j] == 3:
                goal_i = i
                goal_j = j

    di = [0, 0, 1, -1]
    dj = [-1, 1, 0, 0]

    visited[now_i][now_j] = 1
    dfs(now_i, now_j)

    print(f'#{tc+1} {visited[goal_i][goal_j]}')
```



#### :page_with_curl: 백트랙킹

​	해를 찾는 도중에 막히면(즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법

백트랙킹 기법은 최적화 문제와 결정 문제를 해결

결정 문제: 문제의 조건을 만족하는 해가 존재하는지의 여부를 yes or no로 답하는 문제

##### :heavy_check_mark: 깊이우선탐색과의 차이 

​	백트랙킹은 불필요한 경로를 조기에 차단			(가지치기)

​	깊이우선탐색을 재귀로 구현하고 거기에 중단 조건을 추가

##### 	1) 종료조건 2) 원하는 값 3) 분기



##### :pencil2: 부분집합 구하기

```python
def dfs(now = 0, sum = 0, path = []):
    if sum == 10:
        ans_set.add(tuple(path))
        return
    
    if sum > 10:
        return # 가지치기
    
    if now == len(arr):
        return

    if sum + arr[now] <= 10 :
        dfs(now + 1, sum + arr[now], path + [arr[now]])

    dfs(now + 1, sum, path)


arr = [1,2,3,4,5,6,7,8,9,10]
ans_set = set()
dfs()
for ans in ans_set:
    print(ans)
```

```python
powerset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = 10


def dfs(now, resultset):

    if sum(resultset) == 10:
        print(resultset)

    if sum(resultset) > 10:
        return

    for i in range(1, 10):
        next = now + i

        if next >= n:
            continue

        dfs(next, resultset + [powerset[next]])

result = []
for i in range(n):
    dfs(i, result + [powerset[i]])
```







---

#####  문제로 dfs 정리하기



#### :pear: 최소합 찾기!



##### :watermelon: 기본 dfs  ( + backtracking)

```python
def dfs(now_i=0, now_j=0, sum=0):
    global ans

    if now_i == n-1 and now_j == n-1:
        if sum < ans:
            ans = sum
        return

    if sum > ans:				# 가지치기 (백트랙킹)
        return

    for k in range(4):
        next_i = now_i + di[k]
        next_j = now_j + dj[k]

        if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
            continue

        dfs(next_i, next_j, sum + MAP[next_i][next_j])

T = int(input())
for tc in range(T):
    n = int(input())
    MAP = [list(map(int, input().split())) for _ in range(n)]

    di = [0, 0, -1, 1]
    dj = [1, -1, 0, 0]

    ans = 2e18
    dfs(0, 0, MAP[0][0])
    print(ans)
```

##### 	가지치기 한줄로도 시간이 엄청 줄어듬!!



##### :watermelon: dp를 이용

```python
def dfs(now_i=0, now_j=0):
    if now_i == n-1 and now_j == n-1:
        return MAP[now_i][now_j]

    if dp[now_i][now_j] != -1:          # 계산한 적이 있다면
        return dp[now_i][now_j]

    ret = 552341235
    for k in range(4):
        next_i = now_i + di[k]
        next_j = now_j + dj[k]

        if next_i < 0 or next_i >= n or next_j < 0 or next_j >= n:
            continue
        ret = min(ret, dfs(next_i, next_j) + MAP[now_i][now_j])
    dp[now_i][now_j] = ret
    return ret

T = int(input())
for tc in range(T):
    n = int(input())
    MAP = [list(map(int, 
                    input().split())) for _ in range(n)]
    dp = [[-1] * n for _ in range(n)]

    di = [0, 1]
    dj = [1, 0]

    print(dfs(0, 0))
```

##### 	dp는 진짜 엄청 빨름..
