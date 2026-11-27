from itertools import product

alf = sorted('акцент')

n = 1
for i in product(alf, repeat=5):
    if n % 2 == 0 and i[0] not in 'аек' and 'т' in i:
        print(n, i)
        exit(0)
    n += 1