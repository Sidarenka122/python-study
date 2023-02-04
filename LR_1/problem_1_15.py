# Определить есть ли среди заданных целых чисел A, B, C, D хотя бы одно чётное.

A = int(input("Enter A: "))
B = int(input("Enter B: "))
C = int(input("Enter C: "))
D = int(input("Enter D: "))
Array = [A, B, C, D]

EvenExists = False

for n in range(len(Array)):
    if Array[n] % 2 == 0:
        EvenExists = True

print("Exists " if EvenExists else "Not Exists")
