import random

N = 5

numbers = []
for i in range(N):
    numbers.append(random.randint(-10, 10))
print(numbers)

is_init = False
for x in numbers:
    if x % 2 == 0:
        if not is_init:
            min_even = x
            is_init = True
        elif min_even > x:
            min_even = x
if is_init:
    print(min_even)
else:
    print('No even numbers...')
