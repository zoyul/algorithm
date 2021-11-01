# Algorithm 정리



## :bookmark_tabs: 정렬



##### :whale2: 버블정렬 

​	하나씩 비교하면서 큰 값을 오른쪽으로 밀기

```python
n = int(input())
numbers = list(map(int, input().split()))

#버블정렬로 하나씩 비교
for i in range(n-1):
    for j in range(n-i-1):     # range(n-1)[::-1] 도 가능
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
```



##### :whale2: 카운팅정렬

숫자를 count해서 그 숫자를 idx로 하는 list에 저장, 누적 list를 구한 후 숫자 정렬

```python
data = [0, 4, 1, 3, 1, 2, 4, 1]
n = 4
counts = [0] * (n+1)

for i in data:
    counts[i] += 1

# 누적
for i in range(1, n+1):
    counts[i] += counts[i-1]

# 정렬 (뒤에서부터)
num = [0] * len(data)
for i in data[::-1]:
    num[counts[i]-1] = i
    counts[i] -= 1

print(num)
```



##### :whale2: 선택정렬

​		구간을 줄여가면서 최소값을 찾고 맨 왼쪽 값과 교환

```python
n = int(input())
numbers = list(map(int, input().split()))


for i in range(n-1):                      # n-1 번 반복
    min_idx = i                           # 최소는 맨앞으로 잡아두고
    for j in range(i+1, n):
        if numbers[j] < numbers[min_idx]:
            min_idx = j
    numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]

print(numbers)
```



---

#### :bookmark_tabs: 2차원 배열



##### :whale2: 델타

```python
di = [-1, 0, 0, 1] # 위 오 아래 왼
dj = [0, 1, 0, -1]

arr = []

for i in range(len(arr)):
    for j in range(len(arr)):
        testI = i + di[mode]
        testJ = j + dj[mode]
```



##### :whale2: 전치 행렬

​	 대각선을 기준으로 바꾸는거

```python
n = 3
arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(n):
    for j in range(n):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
print(arr)
```



##### :whale2: 이진검색

​	정렬되어있을 때만 가능

```python
def binarySearch(a, key):
    start = 0
    end = len(a)-1

    while start <= end:
        middle = (start + end)//2
        if a[middle] == key:         #검색성공
            return True
        elif a[middle] > key:
            end = middle-1
        else:
            start = middle +1
    return False                   #검색실패
```

* 재귀

```python
def binarySearch2(a, low, high, key):
    if low > high:                      #검색실패
        return False
    else:
        middle = (low + high)//2
        if key == a[middle]:
            return True
        elif key < a[middle]:
            return binarySearch(a, low, middle-1, key)
        else:
            return binarySearch(a, middle+1, high, key)
```

