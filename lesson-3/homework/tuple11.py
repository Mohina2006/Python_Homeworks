my_tuple = (1, 1, 2, 3, 1, 3, 4, 1)
element = 1

index1 = my_tuple.index(element)

index2 = my_tuple.index(element, index1 + 1)

index3 = my_tuple.index(element, index2 + 1)

index4 = my_tuple.index(element, index3 + 1)
print(index1, index2, index3, index4)  