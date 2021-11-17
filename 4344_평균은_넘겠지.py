# https://www.acmicpc.net/problem/4344

def cal_occ(lst):
    divisor = lst[0]
    avg_score = sum(lst[1:])/divisor
    occ = len([j for j in lst[1:] if j > avg_score]) * 100 / divisor
    print(f'{occ:.3f}%')

for cases in range(int(input())):
    lst = list(map(int,input().split()))
    cal_occ(lst)



exec(int(input())*'b,*c=map(int,input().split());print(f"{sum(b*i>sum(c)for i in c)/b:.3%}");')