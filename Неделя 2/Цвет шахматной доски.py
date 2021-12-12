# Заданы две клетки шахматной доски.
# Если они покрашены в один цвет, то выведите слово YES, а если в разные цвета – то NO.

a = int(input())
a1 = int(input())
b = int(input())
b2 = int(input())
if ((a + a1) % 2) == ((b + b2) % 2):
    print('YES')
else:
    print('NO')
