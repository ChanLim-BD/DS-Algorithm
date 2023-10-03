x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}

print(x.__dir__())
print()

print(x)
print()

print(x.get('a'))
print()

print(x.setdefault('e'))
print()

print(x)
print()

print(x.pop('a'))
print(x)
print()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.popitem())
print(x)
print()

x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(x.keys())
print(x.items())
print(x.values())
print()

for i in x:
    print(i, end=' ')
print()

for key, value in x.items():
    print(key, value)