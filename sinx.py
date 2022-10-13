from math import pi, sin

EPS = 1e-6
x = float(input('x[deg]='))
xrad = x/180*3.14159
an_1 = 0
an = xrad
sinx = 0
counter = 3
sign = -1
while abs(an-an_1) >= EPS:
    sinx += an
    an_1, an = an, an*sign*xrad**2/(counter*(counter-1))
    counter += 2
    sign *= -1

print(f'SIN({x})={sinx}\nsin({x})={sin(xrad)}')
