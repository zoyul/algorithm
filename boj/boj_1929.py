# 에라토스테네스의 체

m, n = map(int, input().split())

check = [1] * (n+1)

check[1] = 0
for i in range(2, int(n**0.5) + 1):
    if check[i]:        # 아직 지우지 않았다면
        for j in range(i+i, n+1, i):
            check[j] = 0

for i in range(m, n+1):
    if check[i]:
        print(i)

# 해당 수의 배수를 모두 0으로 만드는 알고리즘 > 그러면 소수만 남음