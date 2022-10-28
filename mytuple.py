t = 1, 2, 3, 1
print(type(t), t)
print(len(t))
print(t.index(1), t.count(1))
x, y, z, w = t
print(x, y, z, w)

t = tuple(([1, 2], [2, 3], 3))
print(type(t), t)
t[0][1] = 11
t[0].append(22)
print(t)
t = tuple([[1, 2], [2, 3], 3])
print(type(t), t)
