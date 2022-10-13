import random

N = 5

numbers = []
for i in range(N):
    numbers.append(random.randint(-10, 10))
print(numbers)

max_el = max(numbers)

counter = 0
for x in numbers:
    if max_el==x:
        counter+=1

print('Max element is',max_el,'Count is',counter)