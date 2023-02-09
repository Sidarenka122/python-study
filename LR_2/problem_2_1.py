# В матрице найти номер строки, сумма чисел в которой максимальна.
import numpy as np

A = np.array([[4, 2, 6, 11],
              [-15, 88, 9, -9],
              [116, 7, 1, 2]])


def summarize(a):
    return sum(a)


mappedArray = list(map(summarize, A))
print(f"mappedArray {mappedArray}")

maxIndexRow = mappedArray.index(max(mappedArray))
print(f"maxIndexRow {maxIndexRow}")
