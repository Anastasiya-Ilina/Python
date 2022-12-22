def summa():
    ''' Функция сложения чисел, введенных в строку через пробел

    Принимает строку из чисел
    Выводит сумму чисел
    '''

    a = 0
    try:
        n = input().split()
        for i in n:
            a += float(i)
        return print(a)
    except TypeError:
        return print('Давайте складывать числа')
    
    
summa()
