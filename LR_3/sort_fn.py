import random
import datetime
import prettytable  # пакет для таблицы
import matplotlib.pyplot as plt  # библиотека для графика

#4. Функция сортировки выбором select:
#Цикл 1 – по i от 0 до N-1 :		# i - счетчик прохода по списку
#	Действие – объявление переменной m = i;	# m - номер для мин. из неотсортированных
#	Цикл 2 – по j от i до N :		# j - счетчик позиции при проходе по неотсортированной части
#		Условие если A[j]<A[m] :	 # сравнение текущего элемента с текущим минимальным
#			Действие – запоминаем номер обнаруженного нового минимального эл-та m = j
#	Действие – перестановка местами A[m] и A[i]

def SelectSort(A):
    for i in range(len(A)):
        m = i
        for j in range(i, len(A)):
            if A[j] < A[m]:
                m = j
        A[m] = A[i]

# 2. Функция сортировки вставками insert:
# Цикл 1 – по i от 1 до (len(A)):					# i - текущая позиция при проходе по списку
# 	Действие – сохранение t = A[i]		# A[i] - вставляемый элемент
#	Действие – новая  переменная j = i 	# j - позиция в отсортированной части списка
#	Цикл 2 – по j до 0 и A[j-1]  > t:		# j - смещается справа налево, от больших к                       меньшим
#		То A[j] = A[j-1] 				       # эл-ты отсортированной части, большие вставляемого
#		И  j -= 1 			       			# уступают место – сдвигаются (копируются) вправо
#	Иначе – выход из цикла 2		       # j остановится на посл. эл-те, большем вставляемого
#	Действие – A[j] = t			              ы# вставляемый эл-т ставится на освободившееся место
#                                                                          место

def InsertSort(A):
    for i in range(1, len(A), 1):
        t = A[i]
        j = i
        for j in range(j, 0, -1):
            if A[j-1] > t:
                A[j] = A[j - 1]
                j -= 1
            else:
                break
        A[j] = t


def BubbleSort(A):  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A) - 1 - i):
            if A[j] > A[j + 1]:
                a = A[j]
                A[j] = A[j + 1]
                A[j + 1] = a


def QuickSort(A, fst, lst):  # быстрая сортировка
    if fst >= lst:
        return

    # i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst + 1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger + 1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger - 1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller - 1)
    QuickSort(A, first_bigger, lst)


table = prettytable.PrettyTable(["Размер списка", "Время Insert", "Время быстрой", "Время Bubble", "Время Select"])
x = []
y1 = []
y2 = []
y3 = []
y4 = []

for N in range(1000, 5001, 1000):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random() * (max - min) + min)))

    # print(A)

    B = A.copy()
    C = A.copy()
    D = A.copy()
    # print(B)

    # InsertSort(A)
    print("---")
    # print(A)

    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    InsertSort(A)
    print("sorted InsertSort", A)
    t2 = datetime.datetime.now()
    y1.append((t2 - t1).total_seconds())
    print("Insert сортировка   " + str(N) + "   заняла   " + str((t2 - t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B) - 1)
    print("sorted QuickSort", B)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " + str(N) + "   заняла   " + str((t4 - t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    BubbleSort(C)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Bubble   " + str(N) + "   заняла   " + str((t6 - t5).total_seconds()) + "c")

    t7 = datetime.datetime.now()
    SelectSort(D)
    print("sorted Select", B)
    t8 = datetime.datetime.now()
    y4.append((t8 - t7).total_seconds())
    print("Select   " + str(N) + "   заняла   " + str((t8 - t7).total_seconds()) + "c")

    table.add_row([str(N), str((t2 - t1).total_seconds()), str((t4 - t3).total_seconds()), str((t6 - t5).total_seconds()), str((t8 - t7).total_seconds())])
print(table)

# Insert
plt.plot(x, y1, "red")

# Quick
plt.plot(x, y2, "green")

# Bubble
plt.plot(x, y3, "blue")

# Select
plt.plot(x, y4, "purple")
plt.show()
