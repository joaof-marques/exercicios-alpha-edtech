a = 10
b = 10
print(id(a))
print(id(b))
print(id(a) == id(b))
print(a==b)
del a
a = 10
print(id(a))