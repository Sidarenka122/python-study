# Вариант 5
# Найдите наименьший четный элемент списка. Если такого нет, то выведите первый элемент.
# Преобразовать список так, чтобы сначала шли нулевые элементы, а затем все остальные.

from random import randint

arrayLen = 15
array = [randint(0, 10) for i in range(arrayLen)]
print(f"initial array {array}")

evenArray = [el for el in array if el % 2 == 0]
print(f"even array {evenArray}")

minElement = min(evenArray) if len(evenArray) > 0 else array[0]
print(f"min element {minElement}")

transformedArray = [el for el in array if el == 0] + [el for el in array if el != 0]
print(f"transformed aray {transformedArray}")
