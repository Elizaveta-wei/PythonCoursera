# Даны три стороны треугольника a,b,c.
# Определите тип треугольника с заданными сторонами.
# Выведите одно из четырех слов: rectangular для прямоугольного треугольника.
# Acute для остроугольного треугольника.
# Obtuse для тупоугольного треугольника.
# Impossible, если треугольника с такими сторонами не существует (считаем, что вырожденный треугольник тоже невозможен).

a = int(input())
b = int(input())
c = int(input())
if a >= b:
    (a, b) = (b, a)
if b >= c:
    (b, c) = (c, b)
if a >= c:
    (a, c) = (c, a)
if a + b <= c:
    print('impossible')
elif a ** 2 + b ** 2 > c ** 2:
    print('acute')
elif a ** 2 + b ** 2 == c ** 2:
    print('rectangular')
else:
    print('obtuse')
