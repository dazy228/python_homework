a1 = "123"
a2 = "123"
a3 = "123"
print(a1, a2, a3)
print(a1 == a2 == a3)
print(id(a1))
print(id(a2))
print(id(a3))

a1 = int
a3 = float
print(a1 == a2 == a3)
print(id(a1))
print(id(a2))
print(id(a3))
print("------------------------------------------------------")
b1 = 321
b2 = "321"
print(b1, b2)
print(b1 == b2)
print(id(b1))
print(id(b2))
b1 = bool
b2 = bool
print(b1, b2)
print(b1 == b2)
print(id(b1))
print(id(b2))


