# улитка

print("На какой день улитка доползет до вершины вертикального шеста?")
print("P.S все величины вводятся в метрах")
h = int(input("Шест высотой: "))
a = int(input("Поднимается за день: "))
b = int(input("Спускается за: "))
print("Улитка проеодалее данно растояние за:", ((h - a - 1) // (a - b) + 2), "дней")

# доработать слонения дней
