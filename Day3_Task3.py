class Bin:
    def __init__(self,n):
        self.n=bin(n)
        
    def __add__(self,other):
        return self.__class__(self.to_dec() + other.to_dec())

    def __sub__(self,other):
        return self.__class__(self.to_dec() - other.to_dec())

    def __mul__(self,other):
        return self.__class__(self.to_dec() * other.to_dec())

    def __floordiv__(self,other):
        return self.__class__(self.to_dec() // other.to_dec())

    def to_dec(self):
        return int(self.n,2)

    def __str__(self):
        return f'{self.__class__.__name__}: {self.n}'

class Oct(Bin):
    def __init__(self,n):
        self.n = oct(n)

    def to_dec(self):
        return int(self.n,8)

class Hex(Bin):
    def __init__(self,n):
        self.n = hex(n)

    def to_dec(self):
        return int(self.n,16)


n1 = int(input('Число 1: '))
n2 = int(input('Число 2: '))
sys = input('Система счисления: ')

if sys =='Bin':
    s1 = Bin(n1)
    s2 = Bin(n2)
elif sys=='Oct':
    s1 = Oct(n1)
    s2 = Oct(n2)
elif sys=='Hex':
    s1 = Hex(n1)
    s2 = Hex(n2)
print(s1+s2, s1-s2, s1*s2, s1//s2, sep='\n')







