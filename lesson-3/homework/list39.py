my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 3  
indices = range(0, len(my_list), n)
nested_list = [my_list[i:i + n] for i in indices]

print(nested_list)