
class String(str):

    def __init__(self, later):
        self.later = later

    def __str__(self):
        return self.later

    def __add__(self, other):
        sum = str(self.later) + str(other.later)
        return f'Your sum later: {sum}'

    def __sub__(self, other):
        return f"Your sub later: {self.replace(other.later, '')}"


later_1 = input('later one: ')
later_2 = input('later two: ')
later_3 = String(later_1)
later_4 = String(later_2)
later_add = later_3 + later_4
later_sub = later_3 - later_4
print(later_add)
print(later_sub)
