# Создайте функцию, которая принимает на вход неограниченное количество позиционных и именованных аргументов,
# в качестве результата функция должна возвращать только позиционные аргументы с нечетными индексами
# и ключевые, значения которых являются строками

def fu(*args, **kwargs):
    print(args[0::2])
    for keys, value in kwargs.items():
        if type(value) == str:
            print(keys, value)
fu(*input(), a = 2, b = 'bazuka', c = 'Chuck Norris', d = 10)
