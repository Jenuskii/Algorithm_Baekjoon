# https://www.acmicpc.net/problem/11653

l = []
n = int(input())
p = 2
while n - 1:
    if n % p == 0:
        l.append(p)
        n //= p
    else:
        p += 1
for i in l:
    print(i)
