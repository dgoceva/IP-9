s = set([1, 2, 3])
print(type(s), s)
# print(s[0])
# s[0] = 11
for x in s:
    print(x)
s.add(12)
print(s)
if 22 in s:
    s.remove(22)
s.update({11, 12, 13})
print(s)
