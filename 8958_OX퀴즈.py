# https://www.acmicpc.net/problem/8958


for i in [sum(map(lambda x: len(x)*(len(x)+1)//2, input().split('X'))) for _ in range(int(input()))]:
    print(i)


for i in[*open(0)][1:]:
    n=0
print(sum((n:=(n+1)*(j=='O'))for j in i))