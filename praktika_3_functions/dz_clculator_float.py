# Простейший калькулятор c введёнными двумя числами вещественного типа
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию)

a = float(input('Введи первое число: '))
b = float(input('Введи второе число: '))
c = input('Введи знак */-+: ')

def calc1(a, b):
    return a + b
def calc2(a, b):
    return a - b
def calc3(a, b):
    return a * b
def calc4(a, b):
    return a / b

if c == '+':
    print(calc1(a, b))
elif c == '-':
    print(calc2(a, b))
elif c == '*':
    print(calc3(a, b))
else:
    print(calc4(a, b))
