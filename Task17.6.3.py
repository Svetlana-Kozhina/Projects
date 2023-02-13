class Node:  # класс элемента
    def __init__(self, value=None, next_=None):  # инициализируем
        self.value = value  # значением
        self.next = next_  # и ссылкой на следующий элемент

    def __str__(self):
        return "Node value = " + str(self.value)


class LinkedList:  # класс списка
    def __init__(self):  # инициализируем пустым
        self.first = None
        self.last = None

    def clear(self):  # очищаем список
        self.__init__()

    def __str__(self):  # функция печати
        R = ''

        pointer = self.first  # берем первый указатель
        while pointer is not None:  # пока указатель не станет None
            R += str(pointer.value)  # добавляем значение в строку
            pointer = pointer.next  # идем дальше по указателю
            if pointer is not None:  # если он существует добавляем пробел
                R += ' '
        return R

    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def pushright(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value)
            self.last.next = new_node
            self.last = new_node

    def popleft(self):
        if self.first is None:  # если список пустой, возвращаем None
            return None
        elif self.first == self.last:  # если список содержит только один элемент
            node = self.first  # сохраняем его
            self.__init__()  # очищаем
            return node  # и возвращаем сохраненный элемент
        else:
            node = self.first  # сохраняем первый элемент
            self.first = self.first.next  # меняем указатель на первый элемент
            return node  # возвращаем сохраненный

    def popright(self):
        if self.first is None: # если список пустой, возвращаем None
            return None
        elif self.first == self.last: # если список содержит только один элемент
            node = self.first # сохраняем его
            self.__init__() # очищаем
            return node # и возвращаем сохраненный элемент
        else:
            node = self.last # сохраняем последний
            pointer = self.first # создаем указатель
            while pointer.next is not node: # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None # обнуляем указатели, чтобы
            self.last = pointer # предпоследний стал последним
            return node # возвращаем сохраненный

    def __len__(self):
        count = 0
        pointer = self.first
        while pointer is not None:
            count += 1
            pointer = pointer.next
        return count

LL = LinkedList() # создает класс списка

LL.pushright(1) # метод вставляет элемент в конец списка
print("Вставлен элемент в конец списка")
print(LL)
LL.pushleft(2) # метод вставляет элемент в начало списка
print("Вставлен элемент в начало списка")
print(LL)
LL.pushright(3) # метод вставляет элемент в конец списка
print("Вставлен элемент в конец списка")
print(LL)
LL.popright() # метод удаляет элемент из конца списка
print("Удален элемент из конца списка")
print(LL)
LL.pushleft(4) # метод вставляет элемент в начало списка
print("Вставлен элемент в начало списка")
print(LL)
LL.pushright(5) # метод вставляет элемент в конец списка
print("Вставлен элемент в конец списка")
print(LL)
LL.popleft() # метод удаляет элемент из начала списка
print("Удален элемент из начала списка")
print(LL)

print(LL.__len__())
