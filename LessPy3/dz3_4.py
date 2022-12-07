import math
import cmath
print('Стандартный вид квадратного уравнения ax^2+bx+c=0. Просьба ввести коэффициенты а, b, c')
Q = input('Хотите ввести комплексные коэффициенты? (Да/Нет) ')
while Q != 'Нет' and Q != 'Да':
Q = input('Хотите ввести комплексные коэффициенты? (Да/Нет) ')

if Q == 'Да':
a = complex(input('Введите коэффициент a: '))
while a == 0:
print('Данное уравнение является линейным')
a = complex(input('Введите коэффициент a, не равный нулю: '))
b = complex(input('Введите коэффициент b: '))
c = complex(input('Введите коэффициент c: '))
desc = b**2 - 4 * a * c
print('Корни уравнения: ', (-b + cmath.sqrt(desc))/(2 * a), ', ', (-b - cmath.sqrt(desc))/(2 * a))

if Q == 'Нет':
a = float(input('Введите коэффициент a: '))
while a == 0:
print('Данное уравнение является линейным')
a = float(input('Введите коэффициент a, не равный нулю: '))
b = float(input('Введите коэффициент b: '))
c = float(input('Введите коэффициент c: '))
desc = b ** 2 - 4 * a * c
if desc > 0:
print('Корни уравнения: ', (-b + math.sqrt(desc)) / (2 * a), ', ', (-b - math.sqrt(desc)) / (2 * a))
if desc == 0:
print('Корень уравнения: ', (-b / (2 * a)))
if desc < 0:
print('Корней нет')
