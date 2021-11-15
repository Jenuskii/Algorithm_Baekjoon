# https://www.acmicpc.net/problem/1110

def function(num):
    a = num // 10
    b = num - 10 * a
    return int(str(b) + str(a+b)[-1])

cnt = 0
target = int(input())
num = target
while cnt == 0 or num != target:
    num = function(num)
    cnt += 1

print(cnt)