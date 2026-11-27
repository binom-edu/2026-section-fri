from itertools import product

alf = sorted('акцент')

n = 1
for i in product(alf, repeat=5):
    if n % 2 == 0 and i[0] != 'а' and i[0] != 'е' and i[0] != 'к' and i.count('т') > 0:
        print(n, i)
        exit(0)
    n += 1