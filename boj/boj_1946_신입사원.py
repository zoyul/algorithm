import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    app = []
    for _ in range(n):
        a, b = map(int, sys.stdin.readline().split())
        app.append((a, b))

    app.sort()          # 일단 한번 정렬을 해줌

    std = app[0][1]
    cnt = 1
    for i in range(n):
        if app[i][1] < std:           # 면접 등수가 높으면 합격, 기준 갱신
            std = app[i][1]
            cnt += 1

    print(cnt)
    print(app)