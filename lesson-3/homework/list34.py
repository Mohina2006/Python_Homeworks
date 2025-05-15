my_list = [1, 2, 3, 2, 4, 2]
length = len(my_list)
new_list = [my_list[-1]]+my_list[0:length-1]
print(new_list)