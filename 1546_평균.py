# https://www.acmicpc.net/problem/1546


length = int(input())
lst = list(map(int, input().split()))
print(sum(lst)/max(lst)*100/length)


n,*l=map(int,open(0).read().split())
print(sum(l)*100/max(l)/n)