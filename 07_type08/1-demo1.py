alf = sorted('акцент')
n = 1
for c1 in alf:
    for c2 in alf:
        for c3 in alf:
            for c4 in alf:
                for c5 in alf:
                    s = c1 + c2 + c3 + c4 + c5
                    if n % 2 == 0 and c1 != 'а' and c1 != 'е' and c1 != 'к' and s.count('т') > 0:
                        print(n, s)
                        exit(0)
                    n += 1