
class String(str):

    def __init__(self, later):
        self.later = str(later)

    def __str__(self):
        return self.later

    def __add__(self, other):
        return String(str(self) + str(other))

    def __sub__(self, other):
        if str(other) in str(self):
            return String(str(self).replace(str(other), ''))
        return String(self)


later_1 = String('later')
later_2 = String(' one')

print(later_1 + later_2)
print(String('later one') - 'one')
print(String('155755') - 7)
print(String('155755') - '155')
print(type(String('155755') - '155'))
