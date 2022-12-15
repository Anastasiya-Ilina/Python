while True:
    try:
        n = int(input('Сумму скольких чисел ряда Фибоначи надо получить?  '))
        def fibonacci(n):
            if n in (1, 2):
                return 1
            return fibonacci(n - 1) + fibonacci(n - 2)
        print(fibonacci(n))
    except:
        print('Возможно только настуральное число')

    q = input('Попробовать еще? (да/нет) ')
    if q == 'нет':
        break
    while q != 'да':
        q = input('Попробовать еще? (да/нет) ')
  
