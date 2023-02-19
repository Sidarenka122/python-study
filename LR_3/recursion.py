# Реализуйте рекурсивную функцию нарезания прямоугольника
# с заданными пользователем сторонами a и b на квадраты
# с наибольшей возможной на каждом этапе стороной.
# Выведите длины ребер получаемых квадратов и кол-во полученных квадратов.

a = int(input("A side length: "))
b = int(input("B side length: "))


def calcSquares(a, b, count):
    if a <= 0 or b <= 0:
        print("Invalid rectangle sizes")
        print("count: 0")
        return
    if a == b:
        print(f"side a: {a}, side b: {b}")
        count += 1
        print(f"count: {count}")
        return
    if a > b:
        print(f"side a: {b}, side b: {b}")
        count += 1
        return calcSquares(a - b, b, count)
    else:
        print(f"side a: {a}, side b: {a}")
        count += 1
        return calcSquares(a, b - a, count)


calcSquares(a, b, 0)
