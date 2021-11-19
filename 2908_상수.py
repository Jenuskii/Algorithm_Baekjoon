# https://www.acmicpc.net/problem/2908

print(max(map(lambda x: int(''.join(reversed(x))), input().split())))

print(max(input()[::-1].split()))