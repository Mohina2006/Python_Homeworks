my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(my_list)
replace = int(input("Enter a number to replace:"))
replace_with = int(input("Enter a number to replace with:"))
index_found = my_list.index(replace)
my_list.insert(index_found, replace_with)
print(my_list)