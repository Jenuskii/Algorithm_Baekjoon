# https://www.acmicpc.net/problem/2869

A,B,V = map(int, input().split())
val = (V-A)/(A-B) + 1
print(int(val) if val == int(val) else int(val) + 1)

# val2 = - ((A-V)//(A-B)) + 1
# print(val2)