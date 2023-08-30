import math

class Point3D:
    def __init__(self, *args):
        self.lst = list(map(int,args))

    def get_distance(self):
        return round(math.sqrt(pow(self.lst[0],2)+pow(self.lst[1],2)+pow(self.lst[2],2)))

    def get_info(self):
        return f'Точка с координатами ({", ".join(map(str,self.lst))})'

class Point2D(Point3D):
    def get_distance(self):
        return round(math.sqrt(pow(self.lst[0],2)+pow(self.lst[1],2)))

cl = input('Введите класс: ')

if cl == "Point2D":
    p = Point2D(*map(int,input('Введите координаты: ').split()))
elif cl == "Point3D":
    p = Point3D(*map(int,input('Введите координаты: ').split()))

print(p.get_distance(), p.get_info(), sep = '\n')





