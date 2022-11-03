def fib(n):
    result = []
    a, b = 0, 1
    while a <= n:
        result.append(a)
        a, b = b, a+b
    return result


def fib2(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a+b
    return result


if __name__ == '__main__':
    import sys
    print(fib2(int(sys.argv[1])))
    print(sys.argv)
    print(sys.path)
