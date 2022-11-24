class MyParent:
    pass


class MyClass(MyParent):
    i = 12345  # class variable

    def f(self):
        return self.i

    def __init__(self):
        list_data = [1, 2, 3]  # object/instance variable


print(MyClass.i)
print(MyClass.f)
# print(MyClass.f())
obj = MyClass()
print(obj.f())
print(obj.list_data)
# print(MyClass.list_data)
