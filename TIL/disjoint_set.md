## :bookmark_tabs: 서로소 집합(Disjoint-sets)

##### 	( 서로소 집합, 상호배타 집합 )

##### 서로 중복 포함된 원소가 없는 집합들 ( = 교집합이 없다)

##### 집합에 속한 하나의 특정 멤버를 통해 각 집합들을 구분. 이를 대표자(representative)라 함



#### :black_nib: 상호배타 집합 표현 방법

##### 	연결 리스트, 트리

* 트리

  자식 노드가 부모 노드를 가리키며 루트 노드가 대표자



#### :black_nib: 상호배타 집합 연산

##### * Make-Set(x) 

​	유일한 멤버 x를 포함하는 새로운 집합을 생성하는 연산

#####  * Find-Set(x)

​	x를 포함하는 집합을 찾는 연산

##### * Union(x, y)

​	x와 y를 포함하는 두 집합을 통합하는 연산



##### :cactus: Make-Set(x)

```python
def Make_set(x):
    parents = [i for i in range(x + 1)]
```



##### :cactus: Find-Set(x)	                                 (대표원소를 찾는 함수)

```python
# 재귀

def Find(x):
    if x == parents[x]:
        return x
    px = Find(parents[x])
    parents[x] = px
    return px
```

```python
# 반복문

def find(x):
    while x != parents[x]:
        x = parents[x]
    return x
```



##### :cactus: Union(x, y)

```python
def Union(x, y):
    px = Find(x)
    py = Find(y)
    parents[py] = px
```



##### :feet: boj 1717 집합의 연산





#### :star2: 연산의 효율을 높이는 방법

##### 	* Rank를 이용한 Union

​	각 노드는 자신을 루트로 하는 subtree의 높이를 랭크Rank라는 이름으로 저장

​	두 집합을 합칠 때 rank가 낮은 집합을 rank가 높은 집합에 붙임

##### 	* Path compression

​	Find-Set을 행하는 과정에서 만나는 모든 노드들이 직접 root를 가리키도록 포인터를 바꿔줌

