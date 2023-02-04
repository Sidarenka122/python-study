# Найти значение максимального элемента списка.
import random

length = int(input("Enter length \n"))

if length <= 0:
    print("No maximum, sorry")
else:
    Array = [random.randint(0, 100) for n in range(length)]
    maximum = Array[0]
    for n in range(len(Array)):
        print("Element #" + str(n + 1) + " is " + str(Array[n]))
        if Array[n] > maximum:
            maximum = Array[n]
    print("Maximum is " + str(maximum))
