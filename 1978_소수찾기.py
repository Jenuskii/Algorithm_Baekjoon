# https://www.acmicpc.net/problem/1978

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

input()
print(sum(map(lambda x: is_prime(int(x)),input().split())))

