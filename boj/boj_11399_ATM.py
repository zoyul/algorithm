import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))

ans = 0
# 시간이 적게 걸리는 사람 순서대로 정렬해서 계산
for i in range(n):
    ans += sum(nums[:i+1])

print(ans)