n = i = int(input())
exec(f'print(n, "*", i//n, "=", i); i+=n;' * 9)