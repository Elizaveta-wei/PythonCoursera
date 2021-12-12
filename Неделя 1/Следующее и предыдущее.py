# Напишите программу, которая считывает целое число и выводит текст
# Вводится целое число (гарантируется, что число находится в диапазоне от -1000 до +1000)

n = int(input())
print('The next number for the number ', n, ' is ', n+1, '.', sep='')
print('The previous number for the number', n,  'is', n-1,  end='.')
