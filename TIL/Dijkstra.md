## :bookmark_tabs: Dijkstra



##### * 최단경로

##### 	간선의 가중치가 있는 그래프에서 두 정점 사이의 경로들 중에 간선의 가중치의 합이 최소인 경로



##### * 다익스트라(Dijkstra) 알고리즘

###### 	음의 가중치 허용 X

##### * 벨만-포드(Bellman-Ford) 알고리즘

###### 	음의 가중치 허용

##### * 플로이드-워샬(Floyd-Warshall) 알고리즘

###### 	모든 정점들에 대한 최소 비용





#### :wink: Dijkstra 다익스트라 알고리즘

##### 	시작 정점에서 거리가 최소인 정점을 선택해 나가면서 최단 경로를 구하는 방식

##### 	시작정점(s) 에서 끝정점(t) 까지의 최단 경로에 정점 x가 존재함

##### 	이때, 최단경로(최소비용)는 s에서 x까지의 최단 경로와 x에서 t까지의 최단경로로 구성

##### 	탐욕 기법을 사용한 알고리즘 (MST의 프림 알고리즘과 유사)



##### :cactus: 다익스트라 기본

```python
def dijkstra():
    visited = [0] * (v+1)
    dist = [INF] * (v+1)
    dist[0] = 0

    for _ in range(v):
        min_idx = -1
        min_value = INF
        
        # 최소값 찾기
        for i in range(v+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = 1
        
        # 갱신(들러서 가는 것이 바로 가는 것보다 비용이 적다면)
        for i in range(v+1):
            if not visited[i] and dist[min_idx] + adj[min_idx][i] < dist[i]:
                dist[i] = dist[min_idx] + adj[min_idx][i]

    return dist[v]


T = int(input())
for tc in range(T):
    v, e = map(int, input().split())
    INF = 923419834

    adj = [[INF] * (v+1) for _ in range(v+1)]

    for _ in range(e):
        n1, n2, w = map(int, input().split())
        adj[n1][n2] = w

    print(dijkstra())

```



##### :cactus: 다익스트라2

```python
def dijkstra():
    visited = [0] * (v+1)
    dist = [INF] * (v+1)
    dist[0] = 0

    for _ in range(v):
        min_idx = -1
        min_value = INF

        for i in range(v+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = 1

        for cost, to in adj[min_idx]:
            if min_value + cost < dist[to]:
                dist[to] = min_value + cost

    return dist[v]


T = int(input())
for tc in range(T):
    v, e = map(int, input().split())
    INF = 9886243
    adj = [[] for _ in range(v+1)]

    for _ in range(e):
        n1, n2, w = map(int, input().split())
        adj[n1].append((w, n2))

    print(dijkstra())
```



##### :cactus: heap을 이용한 다익스트라

```python
import heapq

def dijkstra():
    visited = [0] * (v+1)
    dist = [INF] * (v+1)
    dist[0] = 0

    hq = []
    heapq.heappush(hq, (0, 0))

    while hq:
        now_cost, now = heapq.heappop(hq)
        if visited[now] != 0:
            continue
        visited[now] = 1
        for cost, to in adj[now]:
            if  now_cost + cost < dist[to]:
                dist[to] = now_cost + cost
            	heapq.heappush(hq, (dist[to], to))

    return dist[v]

T = int(input())
for tc in range(T):
    v, e = map(int, input().split())
    INF = 97892643
    adj = [[] for _ in range(v+1)]

    for _ in range(e):
        n1, n2, w = map(int, input().split())
        adj[n1].append((w, n2))

    print(dijkstra())
```



