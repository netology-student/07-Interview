# Необходимо реализовать класс Stack со следующими методами:
#
# isEmpty - проверка стека на пустоту. Метод возвращает True или False.
# push - добавляет новый элемент на вершину стека. Метод ничего не возвращает.
# pop - удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
# peek - возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
# size - возвращает количество элементов в стеке.
#

class Stack:

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            return None
        removed = self.stack.pop()
        return removed

    def peek(self):
        if len(self.stack) == 0:
            return None
        return self.stack[len(self.stack)]

    def size(self):
        return len(self.stack)