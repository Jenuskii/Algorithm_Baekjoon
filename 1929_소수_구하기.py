# https://www.acmicpc.net/problem/1929

# 기존 is_prime 응용 -> 통과는 했으나 속도가 만족스럽지 못함.
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

m,n = map(int,input().split())
l = [i for i in range(m,n+1) if is_prime(i)]
for p in l:
    print(p)


# 에라토스테네스의 체 -> 훨씬 빨라짐
def Sieve_of_Eratosthenes(n):
    sieve = [False, False] + [True]*(n-1)
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            sieve[2*i::i] = [False] * len(sieve[2*i::i])
    return [i for i in range(2,n+1) if sieve[i]]

m,n = map(int,input().split())
[print(i) for i in Sieve_of_Eratosthenes(n) if i >= m]


##실행속도 빠른 다른 유저 풀이
# m, n = map(int, input().split())
# li = [False] + [True] * ((n - 1) // 2)
# for x in range(1, int(n**.5/2+1)):
#     if li[x]:
#         li[2*x*(x+1)::x*2+1] = [False] * ((((n + 1) // 2) - x * x * 2) // (x * 2 + 1))
# if m <= 2:
#     print(2)
# print('\n'.join([f'{x}' for x, val in zip(range(m+(m&1==0), n+1, 2), li[m//2:]) if val]))