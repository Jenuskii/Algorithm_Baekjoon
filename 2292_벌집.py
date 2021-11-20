# https://www.acmicpc.net/problem/2292

n = int(input())
if n == 1:
    print(1)
elif n < 8:
    print(2)
else:
    cur_len = 2
    a,b = 2,8
    k = 2
    while n >= b:
        a = b
        b += k*6
        cur_len += 1
        k += 1
    print(cur_len)


print(int((int(input())/3-.1)**.5+1.5))