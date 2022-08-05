a1 = "123"
a2 = "123"
a3 = "123"
print("===============================================================")
print("Variable: ", a1, a2, a3)
print("Compare first: ", a1 == a2 == a3)
print("ID first time: ", id(a1), id(a2), id(a3))
print("---------------------------------------------------------------")
a1 = list(a1)
a2 = list(a2)
a3 = list(a3)
print("++++++: ", a1, a2, a3)
print("Compare second: ", a1 == a2 == a3)
print("ID second time: ", id(a1), id(a2), id(a3))
print("===============================================================")
b1 = [3, 2, 1]
b2 = [3, 2, 1]
print("Variable: ", b1, b2)
print("Compare first: ", b1 == b2)
print("ID first time: ", id(b1), id(b2))
print("---------------------------------------------------------------")
b1 = bool(b1)
b2 = bool(b2)
print(b1, b2)
print("Compare second: ", b1 == b2)
print("ID second time: ", id(b1), id(b2))
print("===============================================================")


