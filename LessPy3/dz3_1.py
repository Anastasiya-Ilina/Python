print('Ваш персонаж находится в точке (0;0)')
u = int(input('На сколько шагов идем вверх: '))

if u < 0:
    print('Просьба указать положительное число: ')
    u = int(input('На сколько шагов идем вверх: '))
d = int(input('На сколько шагов идем вниз: '))

if d < 0:
    print('Просьба указать положительное число: ')
    d = int(input('На сколько шагов идем вниз: '))
l = int(input('На сколько шагов идем влево: '))

if l < 0:
    print('Просьба указать положительное число: ')
    l = int(input('На сколько шагов идем влево: '))
r = int(input('На сколько шагов идем вправо: '))

if r < 0:
    print('Просьба указать положительное число: ')
    r = int(input('На сколько шагов идем вправо: '))

print('Ваша новая координата: (', u-d, ':', r-l, ")", sep='')
