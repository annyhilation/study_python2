class Queue:
    def __init__(self):
        self.lst = []
    def push(self,item):
        self.lst.append(item)

    def pop(self):
        element = self.lst[0]
        del self.lst[0]
        return element

    def size(self):
        return len(self.lst)

c_lst = [input('Команда: ') for i in range(0,int(input('Количество команд: ')))]
q = Queue()
i=0
for i in range(len(c_lst)):
    if c_lst[i]=='pop':
        print(q.pop())
    elif c_lst[i]=='size':
        print(q.size())
    else:
        item = int(c_lst[i].replace('push',''))
        q.push(item)


