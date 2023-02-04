# Определить, имеется ли среди трёх чисел a, b и c хотя бы одна пара равных между собой чисел.

array = [int(input("Enter 1st number \n")), int(input("Enter 2nd number \n")), int(input("Enter 3rd number \n"))]
duplicateNumberExists = False

for n in range(len(array)):
    print("element " + str(n + 1) + " is " + str(array[n]))

for n in range(len(array)):
    count = 0

    if duplicateNumberExists:
        print("duplicate number is " + str(array[n]))
        break

    for x in range(len(array)):
        if array[x] == array[n]:
            count += 1
        if count > 1:
            duplicateNumberExists = True
            break

if not duplicateNumberExists:
    print("duplicate number doesn't exist")
