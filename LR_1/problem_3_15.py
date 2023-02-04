# Удалить элементы, индексы которых кратны 3.
import random

length = int(input("Enter length \n"))

Array = [random.randint(0, 100) for n in range(length)]
ResultArray = []

print("**** old values ****")

for n in range(len(Array)):
    print(str(Array[n]))

for n in range(len(Array)):
    if n % 3 != 0 or n == 0:
        ResultArray.append(Array[n])

Array = ResultArray

print("**** new values ****")

for n in range(len(Array)):
    print(str(Array[n]))
