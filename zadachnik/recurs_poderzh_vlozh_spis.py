# Вычисление суммы чисел с поддержкой вложенных списков
# Если нужно, чтобы рекурсивная функция обрабатывала вложенные списки, то в теле функции нужно реализовать цикл
# обхода элементов списка.
# Затем этот элемент нужно проверять, является ли он списком по образцу

# Рекурсивная функция - возвращает сумму чисел, обрабатывает вложенные списки
def CalcSumNumbers(A):
    summ = 0

    # здесь нужно реализовать обход в цикле
    for t in A:
        # Обрабатывается элемент t
        if not isinstance(t, list): # проверить, есть ли t списком
            summ = summ + t # если t - не список, то прибавить его к сумме
        else:
            # получить сумму из следующих рекурсивных вызовов
            summ = summ + CalcSumNumbers(t)

    return summ

# Демонстрация использования функции CalcSumNumbers()
# 1. Создать набор чисел
L = [ -2, 3, 8, 11, [-4, 6, [ 2, [-5, 4] ] ] ]

# 2. Вызвать функцию
summ = CalcSumNumbers(L)

# 3. Распечатать сумму
print("summ = ", summ)