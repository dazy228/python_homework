values = [1, 2, '3', 'forth', 'end', 99, True, None]
values_str = []

values_int = list(map(lambda item: str(item) if type(item) == int else values_str.append(item), values))

values_int = [item for item in values_int if item is not None]

print(values_int)
print(values_str)