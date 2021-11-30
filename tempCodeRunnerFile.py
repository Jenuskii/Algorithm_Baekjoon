def Sieve_of_Eratosthenes(n):
    sieve = [False, False] + [True]*(n-1)
    for i in range(2,int(n**0.5)+1):
        if sieve[i]:
            sieve[2*i::i] = [False] * len(sieve[2*i::i])
    return [i for i in range(2,n+1) if sieve[i]]

for i in range(1,100):
    print(i,':',Sieve_of_Eratosthenes(i))
    input()