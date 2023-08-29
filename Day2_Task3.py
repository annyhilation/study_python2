class Queue(list):
    def front(self):
        super().__init__(lst)
        e_null = lst[0]
        self.lst = lst.pop(0)
        return f'Ушел из очереди: {e_null}'

    def get_info(self):
        return f'В очереди {len(lst)} человек: {", ".join(map(str,lst))}. Следующий в очереди: {lst[0]}'


n = int(input('Введите количество человек в очереди: '))
lst=[input('Введите имя человека в очереди: ') for i in range (0, n)]

q = Queue()
print(q.front(),q.front(), sep = '\n')
print(q.get_info())

