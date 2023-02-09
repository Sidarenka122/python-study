# Вариант 3
# Найдите сумму отрицательных элементов списка.
# Найдите сумму элементов списка между двумя первыми нулями.
# Если двух нулей нет в списке, то выведите ноль.

from random import randint

arrayLen = 15
array = [randint(-1, 10) for i in range(arrayLen)]

print(f"initial array {array}")

negativeArraySum = sum([el for el in array if el < 0])

print(f"negativeArraySum {negativeArraySum}")

try:
    firstZeroPosition = array.index(0)

    print(f"firstZeroPosition {firstZeroPosition}")
    print(f"slicedArray - {array[firstZeroPosition + 1:len(array)]}")

    secondZeroPosition = array[firstZeroPosition + 1:len(array)].index(0) + firstZeroPosition + 1

    print(f"secondZeroPosition {secondZeroPosition}")
    print(f"array to sum {array[firstZeroPosition + 1:secondZeroPosition]}")
    print(f"sum {sum(array[firstZeroPosition + 1:secondZeroPosition])}")
except:
    print(f"exception - 0")
