def add(a, ll=[]):
    ll.append(a)
    return ll


def add1(a, ll=None):
    if ll is None:
        ll = []
    ll.append(a)
    return ll


def sum_numbers(*numbers):
    return sum(numbers)


def concat(*data, sep=','):
    return sep.join(data)


print(add(1))
print(add(2))
print(add(3))

print(add1(1))
print(add1(2))
print(add1(3))

print(sum_numbers(1, 2, 3))
print(sum_numbers(1, 2))
print(sum_numbers(1))

print(concat('a', str(1), str(12.2)))
