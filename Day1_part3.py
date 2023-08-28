class Polygon():
    def __init__(self, *args):
        self.pol_l = list(args)

    def __len__(self):
        return len(self.pol_l)

inp = input('Введите длины сторон: ')

plgn = Polygon(*(map(int, inp.split())))
print('Результат функции __len__: ',plgn.__len__())