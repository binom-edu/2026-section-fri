from itertools import product

alf = 'abcx'

ans = 0
for s in product(alf, repeat=5):
    if 'x' not in s or s.count('x') == 1 and s[-1] == 'x':
        ans += 1
print(ans)