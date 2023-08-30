class Student(str):
    def get_action(self):
        return f'Ученик {self.rsplit(":")[1]} учится'

class Teacher(Student):
    def get_action(self):
        return f'Учитель {self.rsplit(":")[1]} учит'

lst = [input('Введите класс и имя: ') for i in range(0,int(input('Введите количество строк: ')))]

for i in range(len(lst)):
    index = lst[i].find("Student")
    if index==-1:
        person = Teacher(lst[i])
        print(person.get_action())
    else:
        person = Student(lst[i])
        print(person.get_action())