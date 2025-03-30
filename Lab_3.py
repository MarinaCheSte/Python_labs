
#1 Используя функцию map() переписать функцию
#items = [1, 2, 3, 4, 5]
#squared = []
#for i in items:
#    squared.append(i**2)

items=[1,2,3,4,5]
mapped_squared=list(map(lambda i:i**2, items))
print(mapped_squared)

#2. Используйте функцию reduce() и перепишите код
#product = 1
#list = [1, 2, 3, 4]
#for num in list:
#    product = product * num

from functools import reduce
num_list = [1,2,3,4]
print(reduce(lambda x,y: x*y, num_list))

#3 Используйте функцию map() и перепишите код
#numbers = [1, 2, 3, 4, 5]
#squared = []
#for num in numbers:
#       squared.append(num ** 2)
#print(squared)

numbers=[1,2,3,4,5]
mapped_numbers=list(map(lambda num: num**2, numbers))
print(mapped_numbers)

#4 Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()
x = [1, 2, 3]
y = [4, 5, 6]
zipped_list=list(zip(x, y))
print(zipped_list)

#5 Используйте функцию zip() чтобы преобразовать код:
#for i in range(len(name_hero)):
#    print(name_hero[i], '-', name_real[i])
name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]

name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]

joint_names = list(map(" - ".join, zip(name_hero, name_real)))
print(joint_names)

# 6 С помощью функции filter() переместите из
# списка numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы в новый список.

all_numbers = [1, 2, 4, 5, 7, 8, 10, 11]
def filter_odd_num(i):
    if(i % 2) != 0:
        return True
    else:
        return False
odd_numbers = list(filter(filter_odd_num, all_numbers))
print(odd_numbers)

