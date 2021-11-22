# https://www.acmicpc.net/problem/1193

def which_group(n):
    a,b = 1,2
    group = 1
    while not(a <= n < b):
        group += 1
        a = b
        b += group
    return group, n - a

def solution(X):
    group, idx = which_group(X)
    l = [i for i in range(1,group+1)]
    if group % 2 == 0:
        top = l[idx]
        bottom = l[-(idx+1)]
    else:
        top = l[-(idx+1)]
        bottom = l[idx]
    return f'{top}/{bottom}'

print(solution(int(input())))

####

n=int(input())
a=0
while n>0:
    a+=1
    n-=a
print("%d/%d"%(1-n,a+n)[::a%2*2-1])