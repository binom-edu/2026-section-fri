def to3(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n //= 3
    return s

def r(n):
    n3 = to3(n)
    if n % 3 == 0:
        n3 += n3[-2:]
    else:
        n3 += to3((n % 3) * 5)
    return int(n3, 3)

ans = 10**9
for n in range(1, 10000):
    if r(n) > 133 and r(n) < ans:
        ans = r(n)
print(ans)