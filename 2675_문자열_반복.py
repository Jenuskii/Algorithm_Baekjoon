# https://www.acmicpc.net/problem/2675

for _ in range(int(input())):
    result = ''
    n, s = input().split()
    for i in map(lambda x: x*int(n), s):
        result += i
    print(result)



for r,_,*s,_ in[*open(0)][1:]:
    print(''.join(c*int(r) for c in s))