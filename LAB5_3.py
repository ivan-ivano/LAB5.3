# < Іваньо Іван >
# Лабораторна робота № 5.3
# Функції, що містять розгалуження та цикли з рекурентними співвідношеннями.
# Варіант 0.6

import math

kp = float(input("kp: "))
kk = float(input("kk: "))
n = float(input("n: "))

print('--------------------')
print('|   k   |   j(x)  |')
print('--------------------')


def j(x):
    if abs(x) >= 1:
        return (math.sin(x + 1))/((math.cos(x + math.exp(x))) ** 2)
    else:
        k = 0
        a = 1
        s = a
        while True:
            k += 1
            r = (2 * x * x) / (k * (2 * k - 1))
            a *= r
            s += a
            if k < 7:
                break
    s *= 1 / (math.cos(2 * x))
    return s


dk = (kk - kp) / n
k = kp

while k <= kk:
    z = j(k) + j(k - 1) ** 2 + 2 * j(1)
    print('|   {0}   |   {1}   |'.format(str(round(k, 4)), str(round(z, 4))))
    k += dk


print('--------------------')
