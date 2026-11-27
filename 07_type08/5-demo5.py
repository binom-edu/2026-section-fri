from itertools import product

alf = sorted('акцент')

for n, i in enumerate(product(alf, repeat=5), start=1):
    s = ''.join(i)
    if n % 2 == 0 and s[0] not in 'аек' and 'т' in s:
        print(n, s)
        exit(0)
