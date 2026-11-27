ans = 0
for x in range(15**4, 15**5):
    c8 = cgt9 = 0
    while x:
        d = x % 15
        if d == 8: c8 += 1
        if d > 9: cgt9 += 1
        x //= 15
    if c8 == 1 and cgt9 > 1:
        ans += 1
print(ans)