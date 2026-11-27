ans = 0
bad = ['16', '36', '56', '76', '61', '63', '65', '67']
for x in range(8**4, 8**5):
    s = oct(x)[2:]
    if s.count('6') == 1 and all(i not in s for i in bad):
        ans += 1
print(ans)