def fib(count):
    a, b = 0, 1
    result = []
    for i in range(count):
        result.append(b)
        a, b = b, a+b
    return result


print(fib(10))
print(fib(100))
