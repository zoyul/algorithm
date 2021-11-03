## :bookmark_tabs:  Stack



* 물건을 쌓아 올리듯 자료를 계속 쌓아 올린 형태의 자료구조
* 스택에 저장된 자료는 선형 구조를 갖는다.
* 마지막 삽입한 자료를 가장 먼저 꺼낸다 (후입선출)



* 1차원 배열을 사용하여 구현하면 구현이 용이하지만, 스택의 크기를 변경하기 어려움
  * 해결 :  저장소를 동적으로 할당하여 스택을 구현(동적 연결리스트)
  * 구현이 복잡하지만 메모리를 효율적으로 사용할 수 있음



#### :black_nib: 스택의 주요 연산

* 삽입 : 저장소에 자료를 저장 (push)
* 삭제 : 저장소에서 자료를 꺼냄(pop)
* isEmpty : 스택이 공백인지 아닌지
* peek : 스택의 top에 있는 원소 item을 반환하는 연산



#### :black_nib: 스택의 pop 알고리즘

```python
def pop() :
    if len(s) == 0:
        return
    else:
        return s.pop(-1)
```



#### :black_nib: 기본 스택 구현

```python
s = []
s.append(1)
s.append(2)
s.append(3)

while s:
    print(s.pop())

#출력
3
2
1
```



#### :black_nib: 스택의 응용

* 괄호검사

* Function call

  *  프로그램에서의 함수 호출과 복귀에 따른 수행 순서 관리

    * 가장 마지막에 호출된 함수가 가장 먼저 실행을 완료, 복귀하는 후입선출 구조

    * 함수 호출 발생 : 호출한 함수 수행에 필요한 지역변수, 매개변수, 수행 후 복귀할 주소 등의 정보를 스택에 저장

    * 함수 실행이 끝나면 시스템 스택의 top을 삭제하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀

      

#### :black_nib: Memoization

​	컴퓨터 프로그램을 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도를 빠르게 하는 기술로 동적계획법(DP)의 핵심이 됨

* 재귀호출!
  * 자기 자신을 호출하여 순환 수행
  * 코드가 간결하지만 호출이 어마어마함.... 시간과 메모리 엄청 많이;;
  * ex) factorial
    * fact(4) = 3 X fact(3)
    * fact(3) = 2 X fact(1)
    * fact(1) = 1

##### :pencil2: 재귀로 표현하는 피보나치

```python
# 0 1 1 2 3 5 8 13 ...

def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n-2) + fibo(n-2)

print(fibo(5))
```

​		재귀함수의 단점!! 중복호출이 존재함 시간이 오래걸림

ex) fibo(5) = fibo(4) + fibo(3)

​					fibo(4) = fibo(3) + fibo(2)

​					fibo(3) = fibo(2) + fibo(1)

   * fibo(2) 가 중복적으로 호출됨

     

##### Memoization 을 적용한 알고리즘

```python
def fibo(n):
    global memo
    if n >= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0, 1]
```

```python
# memo의 크기를 미리 정했을 때

def fibo(n):
    global memo
    if n >= 2 and memo[n] == 0:             # 아직 계산되지 않은 값이면
        memo[n] = (fibo(n-1) + fibo(n-2))
    return memo[n]

n = 50
memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1

print(fibo(5))

# 0 1 1 2 3 5 8 13 21
```

##### 밑에 방법이 호출 횟수가 더 적음



#### :black_nib: DP (Dynamic Programming)

​	동적 계획 알고리즘은 그리디 알고리즘과 같이 최적화 문제를 해결하는 알고리즘이다.

입력 크기가 작은 문제드을 모두 해결한 후에 그 해들을 이용하여 보다 큰 크기의 부분 문제들을 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘이다.



1) 문제를 부분 문제로 분할함

2) 가장 작은 부분 문제부터 해를 구한다.

3) 결과를 테이블에 저장하고, 테이블에 저장된 해를 이용하여 상위 문제의 해를 구한다.



ex) 피보나치에 적용

​	fibo(n) = fino(n-1) + fibo(n-2)

​	fibo(n-1) = fibo(n-2) + fibo(n-3)

​	fibo(2) = fibo(1) + fibo(0)

​	

​	즉, fibo(n) 은 fibo(n-1), fibo(n-2), fibo(n-3) ... fibo(2), fibo(1), fibo(0) 의 부분집합으로 나뉨



##### :pencil2: dp로 피보나치 구현

```python
def fibo(n):
    table = [0, 1]

    for i in range(2, n+1):
        table.append(table[i-1] + table[i-2])

    return table[n]

print(fibo(5))

# recursive 방식
```

```python
# table의 크기를 미리 정했을 때

def fibo(n):

    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

n = int(input())
table = [0] * (n+1)
table[0] = 0
table[1] = 1
print(fibo(n))

#iterative 방식
```



##### :heavy_check_mark: Memoization과 차이

 	Memoization은 재귀구조, DP는 반복구조



##### :pencil2: dp로 factorial 구현하기

```python
def fact(n):

    for i in range(1, n+1):
        table[i] = table[i-1] * i
    return table[n]

n = int(input())
table = [0] * (n+1)
table[0] = 1

print(fact(n))

# 1 1 2 6 48 120
```





##### :pencil2:

```python
T = int(input())
for tc in range(T):
    day, m1, m3, y = (map(int, input().split()))
    plan = [0] + list(map(int, input().split()))

    dp = [0] * 13       # 해당 월 까지의 최소값이 저장

    dp[1] = min(m1, plan[1] * day)
    dp[2] = dp[1] + min(m1, plan[2] * day)

    for i in range(3, 13):
        dp[i] = min(dp[i-3] + m3, dp[i-1] + m1, dp[i-1] + plan[i] * day)

    print(f'#{tc+1} {min(dp[12], y)}')
```



#### :black_nib: DFS(깊이 우선 탐색)

####
