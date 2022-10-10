# 10 digits + 26 small latin letters + 26 capital latin letters
import string
base = string.digits + string.ascii_letters

# print(base)
a = int(input('number: '))
b = int(input('base: '))
# print('number='+str(a))
# print('base='+str(b))

result = ''
while a > 0:
    result += base[a % b]  # result = result+base[a%b]
    a //= b   # a = a//b
print(result[::-1])  # print(reversed(result))
