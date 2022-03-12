import sys

n = int(sys.stdin.readline())
info = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    info.append((a, b))

info.sort(key=lambda x: (x[1], x[0]))
end_time = 0

# 끝나는 시간이 가장 빠른 회의를 잡는다
cnt = 0
for i in range(n):
    if info[i][0] >= end_time:
        end_time = info[i][1]
        cnt += 1

print(cnt)