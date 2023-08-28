class RomanNumber():
    def __init__(self, str_number):
        self.number = str_number

    def __str__(self):
        return f"Число {self.number}"
    def __len__(self):
        return len(self.number)
    def __bool__(self):
        return bool(self.number)
inp = input('Введите число в римской системе: ')
rn = RomanNumber(inp)
print(rn.__str__())
print(rn.__len__())
print(rn.__bool__())