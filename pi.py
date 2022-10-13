import math

EPS = 1e-6

sum = 0
an = 1
an_1 = 0
sign = -1
counter = 3

while abs(an-an_1) >= EPS:
    sum += an
    an_1, an = an, sign/counter
    sign *= -1
    counter += 2
sum *= 4
print('PI={0}\npi={1}'.format(sum, math.pi))
