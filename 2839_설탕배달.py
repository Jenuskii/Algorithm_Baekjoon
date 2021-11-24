# https://www.acmicpc.net/problem/2839

n = int(input())
l = [five + (remain // 3) for five in range(n//5,-1,-1) if (remain := n - 5*five) % 3 == 0]
print(min(l) if l else -1)


##
n=int(input())
print(-(n in [4,7]) or n - 2 * n // 5 * 2)