# https://www.acmicpc.net/problem/9020

# class GoldBach:    
#     def __init__(self,lst):
#         self.sieve = self.Sieve_of_Eratosthenes(max(lst))
#         for i in lst:
#             print(*self.pair(i))

#     def Sieve_of_Eratosthenes(self,n):
#         sieve = [False, False] + [True]*(n-1)
#         for i in range(2,int(n**0.5)+1):
#             if sieve[i]:
#                 sieve[2*i::i] = [False] * ((n // i) - 1)
#         return sieve
    
#     def pair(self,n):
#         start = n // 2
#         i = 0
#         while True:
#             if self.sieve[start-i] and self.sieve[start+i]:
#                 return (start-i, start+i)
#             i += 1

# GoldBach([int(input()) for _ in range(int(input()))])

l = [int(input()) for _ in range(int(input()))]
mx = max(l)
sieve = [False, False] + [True] * (mx - 1)
for i in range(2,int(mx**0.5)+1):
    if sieve[i]:
        sieve[2*i::i] = [False] * ((mx // i) - 1)

for n in l:
    start = n // 2
    i = 0
    while True:
        if sieve[start - i] and sieve[start + i]:
            print(start-i, start+i)
            break
        i += 1