import math
print('Стандартный вид квадратного уравнения ax^2+bx+c=0. Просьба ввести коэффициенты а, b, c')
a = float(input('Введите коэффициент a: '))
while a == 0:
print('Данное уравнение является линейным')
a = float(input('Введите коэффициент a, не равный нулю: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))
desc = b**2 - 4 * a * c
if desc > 0:
print('Корни уравнения: ', (-b + math.sqrt(desc))/(2 * a), ', ', (-b - math.sqrt(desc))/(2 * a))
if desc == 0:
print('Корень уравнения: ', (-b / (2 * a)))
if desc < 0:
print('Корней нет')
