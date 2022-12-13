from random import randint

N = int(input('Введите число значений в последовательности: '))
L = int(input('Введите максимально возможное значение в последовательности: '))
a = []
for i in range(N):
    a.append(randint(1, L))
print('Случайная последовательность:', a)

for i in range(N - 1):
    for j in range(N - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print('Отсортированная последовательность: ', a)
