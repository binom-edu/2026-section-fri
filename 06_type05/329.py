def r(n):
    b = bin(n)[2:]
    if n % 3 == 0:
        b += '010'
    else:
        b += bin(5 * (n % 3))[2:]
    return int(b, 2)

ans = 10**9
for n in range(1, 10000):
    res = r(n)
    if res > 300 and res % 2 == 0 and res < ans:
        ans = res
        print(n, res)