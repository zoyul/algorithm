n = int(input())

num = 666
cnt = 0
while 1:
    if '666' in str(num):           # 해당 수에 666이 들어가는지 하나하나 확인
        cnt += 1
    if cnt == n:
        break
    num += 1
print(num)