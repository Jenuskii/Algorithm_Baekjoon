# https://www.acmicpc.net/problem/1157

word = input().upper()
c_set = set(i for i in word)
c_cnt = dict()
for c in c_set:
    c_cnt[c] = word.count(c)
if len(l := [k for k,v in c_cnt.items() if max(c_cnt.values()) == v]) == 1:
    print(*l)
else:
    print('?')


from statistics import *
try:
    t = mode(input().upper())
except:
    t = '?'
print(t)