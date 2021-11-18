# https://www.acmicpc.net/problem/10809

S = input()
print(*[S.find(s) for s in 'abcdefghijklmnopqrstuvwxyz'])

##
print(*map(input().find,map(chr,range(97,123))))