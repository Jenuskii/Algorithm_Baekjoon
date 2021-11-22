# https://www.acmicpc.net/problem/2775

# 처음 풀이(시간초과)
# def function(k,n):
#     if k == 0:
#         return n
#     else:
#         return sum(function(k-1,i) for i in range(1,n+1))

# for case in range(int(input())):
#     print(function(int(input()), int(input())))
# 시간초과 -> 메모리 제한이 넉넉하니 DP 테이블을 활용해보자. (문제에서 제시한 제한: 1 ≤ k, n ≤ 14)

# DP Table 활용, 1 ≤ k, n ≤ 14, 혁신적인 시간단축!!! 통과
dp = [[i for i in range(1,15)]] + [[0 for _ in range(14)] for __ in range(14)]
def function_dp(k,n):
    if dp[k][n-1]:
        return dp[k][n-1]
    else:
        result = 0
        for i in range(1,n+1):
            result += function_dp(k-1,i)
        dp[k][n-1] = result
    return dp[k][n-1]

from sys import stdin
for case in range(int(stdin.readline())):
    print(function_dp(int(stdin.readline()), int(stdin.readline())))


# PyPy3로 통과한 풀이
def function(k,n):
    if k == 0:
        return n
    else:
        result = 0
        for i in range(1, n+1):
            result += function(k-1, i)
        return result

from sys import stdin
for case in range(int(stdin.readline())):
    print(function(int(stdin.readline()), int(stdin.readline())))


## 다른 유저 숏코딩 -> 조합, 함수(클래스)별칭
import math
i=input
for n in[int]*int(i()):
    k=n(i())
    print(math.comb(k+n(i()),k+1))


