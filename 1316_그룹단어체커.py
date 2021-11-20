# https://www.acmicpc.net/problem/1316

from collections import deque
def is_target(string):
    que = deque(map(str,string))
    result = que.popleft()
    while que:
        c = que.popleft()
        if result[-1] != c:
            result += c
    if len(result) == len(set(map(str,string))):
        return True
    else:
        return False

print(sum([is_target(input()) for _ in range(int(input()))]))



print(sum([*x] == sorted(x,key=x.find) for x in open(0))-1)