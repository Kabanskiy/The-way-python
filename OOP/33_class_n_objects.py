class Example:
    def print(self): # селф это ссылка
        print('dorou')

ex = Example() # создaли объект ех класса эксампл
print(ex) # так мы получим область памяти, в которой хранится эксампл обжект(наш класс)
ex_1 = Example()
ex_1.print()

# создали класс. А объектов можно сделать множество