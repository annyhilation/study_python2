class Person:
    def __init__(self, name, age, passport):
        self. name = name
        self.age = age
        self.__passport = passport

    def change_age(self):
        self.age +=1

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self,value):
        if len(str(value))!=10:
            print('Неверный номер паспорта')
        else: self.__passport = value

    def get_info(self):
        self.__passport = str(self.__passport)
        return f'{self.name}, возраст: {self.age}, номер паспорта: {self.__passport.replace(self.__passport[0:6],"*",1)}'
       # return f'{self.name}, возраст: {self.age}, номер паспорта: {self.__passport}'

name = input('Имя: ')
age = int(input('Возраст: '))
passport = int(input('Паспорт: '))
m = input('Метод: ')
p = Person(name,age,passport)
if m == 'change_age':
    p.change_age()
    print(p.get_info())
else:
    p.passport = int(m)
    p.passport
    print(p.get_info())

