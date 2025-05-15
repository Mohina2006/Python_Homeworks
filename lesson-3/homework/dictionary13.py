my_dict = {'name': "Mohina", 'age': 18, 'university': "New Uzbekistan University"}
inverted_dict = {value: key for key, value in my_dict.items()}
print(inverted_dict)