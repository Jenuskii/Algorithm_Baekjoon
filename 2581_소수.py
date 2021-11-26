# https://www.acmicpc.net/problem/2581

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

if (l := [i for i in range(int(input()), int(input())+1) if is_prime(i)]):
    print(sum(l))
    print(l[0])
else:
    print(-1)