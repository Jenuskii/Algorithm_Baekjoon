# https://www.acmicpc.net/problem/2562

idx = 0
max_num = 0
for i in range(1,10):    
    if (num := int(input())) > max_num:
        max_num = num
        idx = i

print(max_num)
print(idx)




lst = [int(input()) for i in range(9)]
print(max(lst))
print(lst.index(max(lst))+1)


print(*max((int(input()),i+1)for i in range(9)))