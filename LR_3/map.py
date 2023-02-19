list1 = ['1', '2']
list2 = list(map(int, list1))
list3 = list(map(lambda x: x * 2, list2))
print(list2)
print(list3)
