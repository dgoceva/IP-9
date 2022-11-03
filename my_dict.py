digits = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}

for k, v in digits.items():
    print(k, '-->', v)

for d in digits:
    print(d)

for d in digits.values():
    print(d)

for d in digits.keys():
    print(d)

for d in digits.items():
    print(d)
    print(d[0], '-->', d[1])
