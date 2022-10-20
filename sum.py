numbers = input().split()
print(numbers)

even = [int(el) for el in numbers if sum(map(int, str(el))) % 2 == 0]
print(even)

print(sum(even))
