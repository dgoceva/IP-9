txt = input('Enter text:').split()
result = [el.upper() if txt.index(el) % 2 != 0 else el.lower() for el in txt]
print(' '.join(result))
