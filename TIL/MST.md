## :bookmark_tabs: 최소 신장 트리(MST : Minimum Spanning Tree)



##### * 그래프에서 최소 비용 문제

​	1) 모든 정점을 연결하는 간선들의 가중치의 합이 최소가 되는 트리

​	2) 두 정점 사이의 최소 비용의 경로 찾기



##### * 신장 트리

​	n개의 정점으로 이루어진 무방향 그래프에서 n개의 정점과 n-1개의 간선으로 이루어진 트리



##### * 최소 신장 트리(MST)

무방향 가중치 그래프에서 신장 트리를 구성하는 간선들의 가중치의 합이 최소인 신장 트리



##### * MST 표현

 인접 행렬에 연결을 1로 표현하던걸 아예 가중치를 넣자

 인접 리스트에 비용을 함께 저장하자



### :black_nib: Prim 알고리즘

​	점을 선택

​	하나의 정점에서 연결된 간선들 중에 하나씩 선택하면서 MST를 만들어 가는 방식

##### 1) 임의 정점을 하나 선택해서 시작

##### 2) 선택한 정점과 인점하는 정점들 중의 최소 비용의 간선이 존재하는 정점을 선택

##### 3) 모든 정점이 선택될 때까지 1, 2 과정을 반복



##### 서로소인 2개의 집합 (2 disjoint-sets) 정보를 유지

##### * 트리 정점들(tree vertices) - MST를 만들기 위해 선택된 정점들

##### * 비트리 정점들(nontree vertices) - 선택되지 않은 정점들



##### :cactus: prim 기본

```python
def prim():
    MST = [0] * (v+1)           # 정점 포함 표시
    key = [INF] * (v + 1)       # 최소가 되는 값
    key[0] = 0                      # 시자점

    for _ in range(v):              # 정점의 개수만큼
        min_idx = -1
        min_value = INF

        # 최소값 찾기
        for i in range(v+1):
            if not MST[i] and key[i] < min_value:       # MST 포함x 값이 작으면
                min_idx = i
                min_value = key[i]
        MST[min_idx] = 1                                # MST에 포함

        # 갱신할 수 있는 것들 갱신
        for i in range(v+1):
            if not MST[i] and adj[min_idx][i] < key[i]:
                key[i] = adj[min_idx][i]

    return sum(key)


T = int(input())
for tc in range(T):
    v, e = map(int, input().split())
    INF = 94725243

    adj = [[INF] * (v+1) for _ in range(v+1)]

    for _ in range(e):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = adj[n2][n1] = w

    print(prim())
```



##### :cactus: heap을 사용한 prim

```python
# prim

import heapq

def prim():
    MST = [0] * (v+1)           # 정점 포함 표시

    hq = []
    heapq.heappush(hq, (0, 0))
    ans= 0

    while hq:
        now_cost, now = heapq.heappop(hq)
        if MST[now] != 0:
            continue
        ans += now_cost
        MST[now] = 1                # 연결

        for cost, idx in adj[now]:
            if not MST[idx]:
                heapq.heappush(hq, (cost, idx))

    return ans

T = int(input())
for tc in range(T):
    v, e = map(int, input().split())

    adj = [[] for _ in range(v+1)]

    for _ in range(e):
        n1, n2, w = map(int, input().split())
        adj[n1].append((w, n2))
        adj[n2].append((w, n1))

    print(prim())
```



### :black_nib: KRUSKAL 알고리즘

​	간선을 선택

 	간선을 하나씩 선택해서 MST를 찾는 알고리즘

##### 1) 최초, 모든 간선을 가중치에 따라 오름차순으로 정렬

##### 2) 가중치가 가장 낮은 간선부터 선택하면서 트리를 증가시킴 ( 사이클이 존재하면 다음으로 가중치가 낮은 간선 선택)

##### 3) n-2 개의 간선이 선택될 때까지 2 반복



##### 사이클이 만들어지지 않도록 하는 것이 포인트

#####  

```python
#def find(x):
#    while p[x] != x:
#        x = p[x]
#    return x

def find(x):
    if x == p[x]:
        return x
    px = find(p[x])
    p[x] = px
    return px

def union(x, y):
    px = p[x]
    py = p[y]
    p[py] = px

T = int(input())
for tc in range(T):
    v, e = map(int, input().split())

    p = list(range(v+1))
    edges = [list(map(int, input().split())) for _ in range(e)]
    edges.sort(key=lambda x: x[2])

    cnt = 0
    ans = 0

    for x, y, w in edges:
        if find(x) != find(y):
            ans += w
            cnt += 1
            union(x, y)
        if cnt == v:
            break

    print(ans)
```





#### :cactus: 기본문제

```python
# prim

def prim(start):
    key = [INF] * (v+1)
    key[start] = 0
    MST = [0] * (v+1)

    for _ in range(v):
        min_idx = -1
        min_value = INF
        for i in range(v+1):
            if not MST[i] and key[i] < min_value:
                min_idx = i
                min_value = key[i]
        MST[min_idx] = 1

        # 갱신할 수 있으면 갱신
        for i in range(v+1):
            if not MST[i] and adj[min_idx][i] < key[i]:
                key[i] = adj[min_idx][i]

    return sum(key)

T = int(input())
for tc in range(T):
    v, e = map(int, input().split())
    INF = 1831012931

    adj = [[INF] * (v+1) for _ in range(v+1)]

    for _ in range(e):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w
        adj[n2][n1] = w

    print(prim(0))
```

```python
# KRUSKAL

def find_set(x):
    while p[x] != x:
        x = p[x]
    return x

def union(x, y):
    px = find_set(x)
    py = find_set(y)
    p[py] = px


T = int(input())
for tc in range(T):
    v, e = map(int, input().split())

    edges = [list(map(int, input().split())) for _ in range(e)]
    edges.sort(key=lambda x: x[2])                     # 가중치 기준으로 오름차순 정렬

    p = list(range(v + 1))

    cnt = 0     # 간선 선택 횟수
    ans = 0     # 가중치 더한 값
    idx = 0     # edges 인덱스

    while cnt < v:
        n1 = edges[idx][0]
        n2 = edges[idx][1]

        if find_set(n1) != find_set(n2):
            union(n1, n2)
            cnt += 1
            ans += edges[idx][2]

        idx += 1
        
    # for n1, n2, w in edges:
    #     if find_set(n1) != find_set(n2):
    #         cnt += 1
    #         ans += w
    #         union(n1, n2)
    #         if cnt == v:
    #             break

    print(f'#{tc+1} {ans}')
```

