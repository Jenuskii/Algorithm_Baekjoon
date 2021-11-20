# https://www.acmicpc.net/problem/2941

s = input()
l = ['dz=', 'c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']
length = 0
for i in l:
    while i in s:
        length += s.count(i)
        s = s.replace(i, ' ',)
print(length + len(s.replace(' ','')))


c=input().count
print(c('')-1-sum(map(c,['-','=','nj','lj','dz='])))

import re
print(len(re.sub('dz=|[ln]j|\w\W','Z',input())))