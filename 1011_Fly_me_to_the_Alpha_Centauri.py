# https://www.acmicpc.net/problem/1011

def solution():
    distance = abs(eval(input().replace(' ','-')))
    if (sqrt := distance ** 0.5) == int(sqrt):
        print(int(sqrt*2 - 1))
    else:
        sqrt = int(sqrt)
        a = sqrt ** 2
        b = (sqrt + 1) ** 2
        if distance - a <= (b - a - 1) // 2:
            print(sqrt * 2)
        else:
            print(sqrt * 2 + 1)
for _ in range(int(input())):
    solution()


##
for i in [int] * int(input()):
    x, y = input().split()
    print(i(2*(i(y)-i(x)-.5)**.5))