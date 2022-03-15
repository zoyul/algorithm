import sys

n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)

ans = []
stack = []
i = 1
j = 0
while i <= n:
    stack.append(i)
    ans.append('+')
    if i == nums[j]:                # 스택에 계속 넣다가 수열에 맞는 수가 나오면 pop
        while stack[-1] == nums[j]:
            stack.pop()
            j += 1
            ans.append('-')
            if len(stack) == 0:
                break
    i += 1

# 스택에 수가 남아있다면 안되는거니까 no 출력
if stack:
    print('NO')
else:
    for e in ans:
        print(e)