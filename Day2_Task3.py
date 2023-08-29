class Queue(list):
    def front(self,lst):
        e_null = lst[0]
        self.lst = lst.pop(0)
        return f'Ушел из очереди: {e_null}'

    def get_info(self, lst):
        return f'В очереди {len(lst)} человек: {", ".join(map(str,lst))}. Следующий в очереди: {lst[0]}'


n = int(input('Введите количество человек в очереди: '))
lst=[input('Введите имя человека в очереди: ') for i in range (0, n)]

q = Queue(lst)
print(q.front(lst),q.front(lst), sep = '\n')
print(q.get_info(lst))

