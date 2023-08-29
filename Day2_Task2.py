class OddEvenList(list):
    def get_even(self, lst):
        self.lst = lst
        return [self.lst[i] for i in range(len(self.lst)) if self.lst[i]%2==0]
        
    def get_odd(self, lst):
        self.lst = lst
        return [self.lst[i] for i in range(len(self.lst)) if self.lst[i]%2!=0] 

n = int(input('Введите количество чисел: '))
lst=[int(input('Введите число последовательности: ')) for i in range (0, n)]

oel = OddEvenList(lst)
print(oel)
print(oel.get_even(lst))
print(oel.get_odd(lst))

