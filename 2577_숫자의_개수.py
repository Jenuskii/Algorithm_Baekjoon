# https://www.acmicpc.net/problem/2577

lst = [0] * 10
A, B, C = (int(input()) for _ in range(3))

for i in str(A*B*C):
    lst[int(i)] += 1

for result in lst:
    print(result)


exec('n,m=0,1'+'*int(input())'*3+';print(str(m).count(str(n)));n+=1'*10)