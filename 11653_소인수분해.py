# https://www.acmicpc.net/problem/11653

def is_prime(n):
    prime = True    
    if n == 2:
        return True
    elif n == 1 or n % 2 == 0:
        return False
    for i in range(3,int(n**0.5)+1,2):
        if n % i == 0:
            prime = False
            break
    return prime

def next_prime(p):
    if p == 2:
        return 3
    else:
        while True:
            p += 2
            if is_prime(p):
                return p


l = []
n = int(input())
p = 2
while n - 1:
    if n % p == 0:
        l.append(p)
        n //= p
    else:
        p = next_prime(p)
for i in l:
    print(i)

############### 시간초과!