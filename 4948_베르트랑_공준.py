# https://www.acmicpc.net/problem/4948

def Sieve_of_Eratosthenes(n):
    sieve = [False, False] + [True]*(n-1)
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            sieve[2*i::i] = [False] * len(sieve[2*i::i])
    return sieve

nums = []
while (n := int(input())):
    nums.append(n)

sieve = Sieve_of_Eratosthenes(max(nums)*2)
for n in nums:
    print(sum(sieve[n+1 : 2*n+1]))

