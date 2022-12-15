def summa():
    a = 0
    try:
        n = input().split()
        for i in n:
            a += float(i)
        return print(a)
    except TypeError:
        return print('Давайте складывать числа')
summa()
