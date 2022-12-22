import io
import math
with io.open('Input.txt', encoding='utf-8') as f:
        a = f.read().split()    # Считывает значения в файле
print('Начальные значения:', a)

C = math.floor(int(a[0])/2)    # Определяет целое число атомов углерода
H = math.floor(int(a[1])/6)    # Определяет целое число атомов водорода
O = math.floor(int(a[2])/1)    # Определяет целое число атомов кислорода

print('Максимально возможно число молекул спирта: ', min(C, H, O))
