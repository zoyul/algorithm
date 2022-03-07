import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())

# 각각 왼쪽 오른쪽에서 움직일 포인터
i = 0
j = n-1

cnt = 0
while i < j:
    if nums[i] + nums[j] == x:
       cnt += 1
       i += 1
       j -= 1
    elif nums[i] + nums[j] > x:
        j -= 1
    elif nums[i] + nums[j] < x:
        i += 1

print(cnt)