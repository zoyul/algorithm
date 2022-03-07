n, k = map(int, input().split())

check = [1] * (n+1)
check[1] = 0

cnt = 0
for i in range(2, n + 1):
    for j in range(i, n+1, i):
        if check[j] == 0:            # 이미 지웠다면 패스
            continue
        cnt += 1
        check[j] = 0

        if cnt == k:            # k번째 수를 지우면 끝
            print(j)
            break