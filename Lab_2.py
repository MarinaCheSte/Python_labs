# Лабораторная 2
# Вариант 2
# Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
# Найдите минимальный по модулю элемент списка.

num_list = list(map(int, input("Введите целочисленные значения через запятую: ").split(',')))

max_odd_num=num_list[0]
min_abs_num=num_list[0]

for num in num_list:
    if num%2!=0 and num>max_odd_num:
        max_odd_num=num
    if abs(min_abs_num)>abs(num):
        min_abs_num=num
print("Список:", num_list)
print("Наибольший нечетный элемент:", max_odd_num)
print("Минимальный по модулю элемент списка:", min_abs_num)

# Вариант 4
# Найдите произведение элементов списка с нечетными номерами.
# Найдите наибольший элемент списка, затем удалите его и выведите новый список.
from math import prod
sum_list = list(map(int, input("Введите значения через запятую: ").split(',')))
print("Весь список:",sum_list)
print("Произведение элементов с нечетными номерами:", prod(sum_list[1::2]))

max_elem=sum_list[0]

for elem in sum_list:
    if elem>max_elem:
        max_elem=elem

sum_list.remove(max_elem)
print("Список без наибольшего элемента:",sum_list)

# Задание 2 Многомерные списки
# 2. Симметричная матрица.
# Дана квадратная матрица. Проверить, является ли она симметричной относительно главной диагонали.

symmetric_matrix = [
    [8, 1, 2],
    [1, 7, 3],
    [2, 3, 6]
]

false_list=[]

n = len(symmetric_matrix)
for i in range(n):
    for j in range(i + 1, n):
        if symmetric_matrix[i][j] != symmetric_matrix[j][i]:
            false_list.append(symmetric_matrix[i][j])

if len(false_list)==0:
    print("Матрица симметрична относительно главной диагонали.")
else:
    print("Матрица несимметрична")




