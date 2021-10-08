a = [*open(0)]
[print(f'Case #{i+1}: {sum(map(int, a[i+1].split()))}') for i in range(int(a[0]))]
