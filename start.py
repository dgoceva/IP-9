# int
# ** * / // % + -
# 1/2 = 0.5
# 1//2 = 0 1%2 = 1

# float
# ** * / + -

import random
print(3/2+1.3)

# relational operations: == != < > <= >=
# boolean
# true false
# X     Y       not X   X and Y     X or Y
# false false   true    false       false
# true  false   false   false       true
# false true            false       true
# true  true            true        true

# char, str(ing)
# +

print(random.randrange(10))
print(random.randrange(-10, 10))

s = 0
s_even = 0
for i in range(5):  # 0 1 2 3 4
    x = random.randint(-10, 10)
    print(x, end=' ')
    s += x
    if x % 2 == 0:  # x % 2 != 0
        s_even += x
print()
print('Sum=', s, sep='')
print('Sum of even numbers:', s_even)
