# Шахматный король ходит по горизонтали, вертикали и диагонали, но только на 1 клетку.
# Даны две различные клетки шахматной доски, определите, может ли король попасть с первой клетки на вторую одним ходом.

a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (c > (a + 1)) or (c < (a - 1)) or (d > (b + 1)) or (d < (b-1)):
    print('NO')
else:
    print('YES')
