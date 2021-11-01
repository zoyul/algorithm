#### 순열

```python
n = 12

for i in range(1, n+1):
    for j in range(i, n+1):
        if j != i:
            for k in range(j, n+1):
                if k != i and k != j:
                    print(i, j, k)
```



#### 부분집합

##### :pencil2: 비트연산

````python
bit = [0, 0, 0, 0]

for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            for l in range(2):
                bit[3] = l
                print(bit)
````

##### :pencil2:  좀 더 간단히

```python
arr = [1, 2, 3, 4, 5]
n = 5

for i in range(1<<n): # n**2랑 똑같은 거임
    print(f'#{i+1}', end=' ')
    for j in range(n):
        if i & (1<<j):
            print(arr[j], end=' ')
    print()
```

