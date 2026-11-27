def f(s):
    global n
    if len(s) == 5:
        n += 1
        if n % 2 == 0 and s[0] != 'а' and s[0] != 'е' and s[0] != 'к' and s.count('т') > 0:
            print(n, s)
            exit(0)
        return
    for c in sorted('акцент'):
        f(s + c)

n = 0
f('')