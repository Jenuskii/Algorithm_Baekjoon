# https://www.acmicpc.net/problem/10250

import sys
for _ in range(int(sys.stdin.readline())):
    h,w,n = map(int, sys.stdin.readline().split())
    col = f'{-((-n)//h):#02d}'
    row = str((n-1) % h + 1)
    sys.stdout.writelines(row+col+'\n')

