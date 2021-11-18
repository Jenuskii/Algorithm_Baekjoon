# https://www.acmicpc.net/problem/1065

def is_target(n):
    if n < 100:
        return True
    else:
        each = list(map(int,str(n)))
        d = each[-1] - each[-2]
        for i in range(len(each)-1):
            if each[i+1] - each[i] != d:
                return False
        return True

cnt = 0
for i in range(1,int(input())+1):
    if is_target(i):
        cnt += 1
print(cnt)

###
print(sum(i<100 or i//100*21+i == i//10*12 for i in range(1,int(input())+1)))