# https://www.acmicpc.net/problem/3052

a = set()
for _ in range(10):
    a.add(int(input()) % 42)
print(len(a))

b = [int(input) % 42 for _ in range(10)]
print(len(set(b)))