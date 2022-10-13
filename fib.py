number = int(input('N='))
fib = []
an, an_1 = 1, 0
for i in range(number):
    fib.append(an)
    an_1, an = an, an_1+an
print(fib)
print(sum(fib))
