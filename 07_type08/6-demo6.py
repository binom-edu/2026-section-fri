from itertools import product

print(*[(n, s) for n, s in enumerate(product(sorted('акцент'), repeat=5), start=1) if n % 2 == 0 and s[0] not in 'аек' and 'т' in s][0])