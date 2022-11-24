def scope_test():
    def do_local():
        spam = 'local test'

    def do_nonlocal():
        nonlocal spam
        spam = 'nonlocal test'

    def do_global():
        global spam
        spam = 'global test'

    spam = 'test'
    do_local()
    print(f'After do_local(): {spam}')
    do_nonlocal()
    print(f'After do_nonlocal(): {spam}')
    do_global()
    print(f'After do_global(): {spam}')


scope_test()
print(f'In global scope: {spam}')
