import math

class Circle():
    def __init__(self, *args):
        coord = list(args)
        self.x = coord[0]
        self.y = coord[1]
        self.R = coord[2]

    def __str__(self):
       return f"Окружность с центром в точке: ({self.x},{self.y}) и радиусом {self.R} "

inp = input('Введите 3 целых числа: ')

crcl = Circle(*(map(int, inp.split())))
print('__str__: ', crcl.__str__())
