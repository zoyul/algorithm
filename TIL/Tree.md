## :bookmark_tabs: Tree





#### :black_nib: 순회

​		트리의 노드들을 체계적으로 방문하는 것

* 전위순회

​		부모노드 방문 후, 자식노드를 좌, 우 순서로

* 중위순회

​		왼족 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문

* 후위순회

​		자식노드를 좌우 순서로 방문한 후, 부모노드로 방문

#### 

##### :whale: 전위순회

```python
def pre_order(n):
    if n:                   # 유효한 정점이면
        print(n)
        pre_order(left[n])
        pre_order(right[n])

v = int(input())
left = [0] * (v+1)
right = [0] * (v+1)
for _ in range(v-1):
    p, s = map(int, input().split())
    if left[p] == 0:
        left[p] = s
    else:
        right[p] = s

pre_order(1)
```



##### :whale: 중위순회

```python
def in_order(n):
    if n:
        in_order(left[n])
        print(n)
        in_order(right[n])

v = int(input())
left = [0] * (v+1)
right = [0] * (v+1)
for _ in range(v-1):
    p, s = map(int, input().split())
    if left[p] == 0:
        left[p] = s
    else:
        right[p] = s

in_order(1)
```



##### :whale: 후위순회

```python
def post_order(n):
    if n:
        post_order(left[n])
        post_order(right[n])
        print(n)


v = int(input())
left = [0] * (v+1)
right = [0] * (v+1)
for _ in range(v-1):
    p, s = map(int, input().split())
    if left[p] == 0:
        left[p] = s
    else:
        right[p] = s


post_order(1)
```



##### :whale: dict로

```python
import sys

def pre_order(x):
    if x == '.':
        return

    print(x, end='')
    pre_order(tree[x][0])
    pre_order(tree[x][1])

def in_order(x):
    if x == '.':
        return

    in_order(tree[x][0])
    print(x, end='')
    in_order(tree[x][1])


def post_order(x):
    if x == '.':
        return

    post_order(tree[x][0])
    post_order(tree[x][1])
    print(x, end='')


n = int(sys.stdin.readline())
tree = {}

for _ in range(n):
    a, b, c = sys.stdin.readline().split()
    tree[a] = [b, c]

pre_order('A')
print()
in_order('A')
print()
post_order('A')
```



##### :whale: list 하나로

```python
def preorder(n):
    if n != 1 and g[n] == 0:
        return

    print(n, end=' ')
    preorder(g[n * 2])
    preorder(g[n*2+1])

    # print(n, end=' ')
    # if g[n*2]:
    #     preorder(g[n*2])
    # if g[n*2+1]:
    #     preorder(g[n*2+1])

T = int(input())
for tc in range(T):
    n = int(input())
    g = [0] * ((n+1) * 2)
    for _ in range(n-1):
        a, b = map(int, input().split())
        if g[a*2] == 0:
            g[a*2] = b
        else:
            g[a*2+1] = b

    print(g)
    preorder(1)
```

