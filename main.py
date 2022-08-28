
from stack import Stack

def check_balance(target_string):
    stack = Stack()

    pairs = {')':'(', '}':'{', ']':'['}

    for s in target_string:
        if s in '({[':
            stack.push(s)
        elif stack.isEmpty():
            return False
        else:
            p = pairs[s]
            if p != stack.pop():
                return False

    return stack.isEmpty()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #  Программа ожидает на вход строку со скобками. На выход сообщение: "Сбалансированно", если строка корректная,
    #  и "Несбалансированно", если строка составлена неверно.

    input_str = input("Введите строку со скобками: ")
    if check_balance(input_str):
        print("Сбалансированно")
    else:
        print("Не сбалансированно")


