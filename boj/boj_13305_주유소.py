n = int(input())
dis = list(map(int, input().split()))
stops = list(map(int, input().split()))

ans = 0
price = stops[0]
for i in range(n-1):
    if stops[i] < price:             # 가격이 크다면 이전에 더 낮은가격으로 주유를 했다고 계산
        price = stops[i]
    ans += price * dis[i]

print(ans)