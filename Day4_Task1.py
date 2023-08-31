class Product:
    def __init__(self, name, price, amount):
        self.name = name
        self.price = price
        self.__amount = 10

    @property
    def amount(self):
        return self.__amount

    @amount.setter
    def amount(self,value):
        self.__amount = value
   # @amount.setter
    def sale(self):
        if self.__amount > 0:
            self.__amount-=1
        else: print('Нет в наличии')

  #  @amount.setter    
    def refund(self):
        self.__amount+=1
        return self.__amount

    def get_info(self):
        return f'Товар: {self.name}, цена: {self.price}, количество: {self.__amount}'

name = input('Товар: ')
price = int(input('Цена: '))
amount = int(input('Количество: '))
m = input('Метод: ')

p = Product(name,price, amount)
if m == 'sale':
 #   p.sale()
 #   print(p.get_info())
    p.amount = amount
    p.sale()
else: 
    p.amount = amount
    p.refund()

print(p.get_info())