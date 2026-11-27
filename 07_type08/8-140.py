from itertools import permutations

ans = set()
for i in permutations('аджика'):
    s = ''.join(i)
    if 'аа' not in s:
        ans.add(s)
print(len(ans))