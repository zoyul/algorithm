## :bookmark_tabs:  문자열



#### :pencil2: 패턴매칭

* 고지식한 패턴 검색 알고리즘
* 카프-라빈 알고리즘
* KMP 알고리즘
* 보이어-무어 알고리즘



##### :whale2:  고지식한 알고리즘

```python
p = 'is'
t = 'This is a book~!'
# t에서 p찾을거임

i = 0
result = 0
while i < len(t) - len(p) + 1:
    cnt = 0
    for j in range(len(p)):
        if t[i+j] == p[j]:             # 문자열 비교 시작
            cnt += 1
        else:
            break
    if cnt == len(p):                     # 비교 횟수가 같으면
        print(i)
        i += len(p)                       # 비교 위치 이동
    else:
        i += 1
print()
```



```python
i, j = 0, 0   #i 는 t의inx, j는 p 의 idx
while i < len(t) and j < len(p):
    if t[i] != p[j]:
        i = i - j            # 비교한 길이만큼 다시 돌아감
        j = -1                # 비교 위치 초기화
    i += 1
    j += 1
if j == len(p):
    print(i - len(p))
else:
    print()
    
# 출력값
# 2
```



```python
i, j = 0, 0   #i 는 t의inx, j는 p 의 idx

while i < len(t) and j < len(p):
    if t[i] != p[j]:
        i = i - j            # 비교한 길이만큼 다시 돌아감
        j = -1                # 비교 위치 초기화
    i += 1
    j += 1
    if j == len(p):
        print(i - len(p))
        j = 0
    # else:
    #     print()
    
# 출력값
# 2
# 5
```





##### :whale2: KMP 알고리즘

* 찾을 문자열의 패턴을 전처리하여 배열을 미리 구함



##### :whale2: 보이어-무어