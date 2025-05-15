my_tuple = (1, 2, 3, 4, 1, 4)
element = 4
index_find = my_tuple.index(4)
new_tuple = my_tuple[0:index_find] + my_tuple[index_find +1:]
print(new_tuple)
