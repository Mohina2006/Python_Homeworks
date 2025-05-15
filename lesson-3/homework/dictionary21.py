my_dict = {'name': 'Mohina', 'age': 19, 'university': 'New Uzbekistan University'}

sorted_dict_by_value = dict(sorted(my_dict.items(), key=lambda item: item[1]))

print(sorted_dict_by_value)
