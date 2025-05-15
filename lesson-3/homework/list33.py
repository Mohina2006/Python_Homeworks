my_list = [1, 2, 3, 2, 4, 2]
element = 2
i1 = my_list.index(element)
i2 = my_list.index(element, i1 + 1)
i3 = my_list.index(element, i2 + 1)

print(i1, i2, i3)  