import math

class PrimeNumbers():
    def __init__(self, n):
        self.n = n
        self.num_list = list()
        number=1
        indic = 0

        while (len(self.num_list)) < n:
            for j in range(1,10):
                number2=j
                if (number%number2 == 0 and number!=number2) and (number%number2 == 0 and number2!=1): #не простое число
                    indic=1
            if indic==0: #если ни разу не попалось условие, при котором число уже не простое, то добавляем его в список и берем следующее число
                self.num_list.append(number)
                number+=1
            else: #иначе просто берем следующее число
                number+=1
            indic=0 #возвращаем индикатору начальное значение
            
    def __str__(self):
        return f"Последовательность из {self.n} простых чисел {self.num_list}"

    def total(self):
        return sum(self.num_list)

num = int(input('Введите количество простых чисел: '))
pm = PrimeNumbers(num)
print(pm.__str__())
print(pm.total())
