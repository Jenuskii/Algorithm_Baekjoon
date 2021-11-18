# https://www.acmicpc.net/problem/4673

def d(n):
    return n + sum([int(i) for i in str(n)])

def all_d(n, limit):
    all_d_set = set()
    next_d = d(n)
    while next_d <= limit:
        all_d_set.add(next_d)
        next_d = d(next_d)
    return all_d_set

answer_set = set(i for i in range(1,10001))
for n in range(1,10001):
    if n in answer_set:
        answer_set -= all_d(n, 10000)

for answer in sorted(answer_set):
    print(answer)





# r=range(9999)
# print(*sorted({*r}-{n+sum(map(int,str(n)))for n in r}))