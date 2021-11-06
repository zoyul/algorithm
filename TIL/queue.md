## :bookmark_tabs:  Queue

 * 스택처럼 삽입과 삭제의 위치가 제한적

 * 선입선출 구조(FIFO: First In First Out)

   가장 먼저 삽입된 원소가 가장 먼저 삭제
   
* 머리(Front), 꼬리(Rear)



#### :black_nib: 큐의 주요 연산

* enQueue: 큐의 뒤쪽(rear) 에 원소 삽입

* deQueue: 큐의 앞쪽(front) 에서 원소를 삭제하고 반환

* createQueue: 공백 상태의 큐 생성

* isEmpty(): 큐가 공백상태인지 확인

* isFull(): 큐가 포화상태인지 확인

* Qpeek(): 큐의 앞쪽(front) 에서 원소를 삭제하지 않고 반환만



#### :black_nib: 선형큐

​	1차원 배열을 이용

​	큐의 크기 = 배열의 크기

* 초기 상태: front = rear = -1
* 공백 상태: front = rear
* 포화 상태: rear = n-1



##### :whale2: 삽입: enQueue

```python
def enQueue(item):
    global rear
    if isFull():
        print('Queue_Full') # 디버깅용
    else:
        rear += 1
        Q[rear] = item
```



##### :whale2: 삭제: deQueue

```python
def deQueue(item):
    global front
    if isEmpty():
        pass
    else:
        front += 1
        print(Q[front])
```



#### :black_nib: 큐 구현 방법

1. front, rear 사용
2. append, pop 사용
3. from collections import dequeue 모듈 사용

#### 

##### :whale2: front, rear 사용

​	속도가 제일 빠름

```python
# 1. 공백 Q 생성
Q = [0] * 10
front, rear = 1, 1

rear += 1
Q[rear] = 1		# enQueue

rear += 1
Q[rear] = 2

rear += 1
Q[rear] = 3

while front != rear:		#dequeue
    front += 1
    print(Q[front], end=' ')
    
# 출력값
1 2 3

# q의 변화
[0, 0, 1, 2, 3, 0, 0, 0, 0, 0]
[0, 0, 1, 2, 3, 0, 0, 0, 0, 0]
[0, 0, 1, 2, 3, 0, 0, 0, 0, 0]
```



##### :whale2: append, pop 사용

​	시간이 오래 걸림(append는 전체를 다시 만들고 붙임)

```python
q = []
q.append(1)
q.append(2)
q.append(3)
while q:
    print(q.pop(0), end = ' ')
    
# 출력값
1 2 3

# q의 변화
[1, 2, 3]
[2, 3]
[3]
```



##### :whale2: deque를 import

```python
from collections import deque

q = deque()

# enqueue -> append <-> appendleft
q.append(1)
q.append(2)
q.append(3)
# dequeue -> popleft
while q:
    print(q.popleft(), end = ' ')
    
# 출력값
1 2 3
```



#### :black_nib: 선형큐

​	1차원 배열

* 초기 공백 상태: front = rear = 0
* 포화 상태: (rear + 1) mod n = front
* index의 순환: 나머지 연산자 mod 사용
* 삽입: rear = (rear + 1) mod n
* 삭제: front = (front + 1) mod n



##### :whale2: 삽입: enQueue

```python
def enQueue(item):
    global rear
    if isFull():
        print('Queue_Full') # 디버깅용
    else:
        rear = (rear + 1) % len(Q)
        Q[rear] = item
```



##### :whale2: 삭제: deQueue

```python
def deQueue(item):
    global front
    if isEmpty():
        pass
    else:
        front = (front + 1) % len(Q)
        print(Q[front])
```



#### :black_nib: 연결 큐

​	단순 연결 리스트의 노드(링크로 연결되어 있음)

* front: 첫 번째 노드를 가리키는 링크
* rear: 마지막 노드를 가리키는 링크
* 초기 상태: front = rear = null
* 공백 상태: front = rear = null



##### :whale2: 연결 큐 구현

```python
class Node:
    def __init__(self, item, n=None):
        self.item = item
        self.next = n
        
def enQueue(item):		# 연결 큐의 삽입 연산
    global front, rear
    newNode = Node(item)	# 새로운  노드 생성
    if front == None:		# 큐가 비어있다면
        front = newNode
    else:
        rear.next = newNode
    rear = newNode

def deQueue(item):
    global front, rear
    if isEmppty():
        print('Queue_Empty')
        return None
    
    item = front.item
    front = front.next
    if isEmpty():
        rear = None
    return item
```



#### :black_nib: 우선순위 큐

​	우선순위를 가진 항목들을 저장하는 큐

​	FIFO 순서가 아니라 우선순위가 높은 순서대로 나간다.

​	원소를 삽입하는 과정에서 우선순위를 비교하여 적절한 위치에 삽입함

​	가장 앞에 최고 우선순위 원소가 위치하게 됨

​	배열을 사용해서 삽입이나 삭제 연산이 일어날 때 원소의 재배치가 발생하며

​	시간이나 메모리 낭비가 큼

* 시뮬레이션 시스템, 네트워크 트래픽 제어, 운영체제의 테스크 스케줄링



#### :black_nib: BFS(너비 우선 탐색)

