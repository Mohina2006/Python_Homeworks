my_dict = {'name': "Mohina", 'age': 18, 'university': "New Uzbekistan University"}
key_to_remove = 'university'

if key_to_remove in my_dict:
    del my_dict[key_to_remove]
else:
    print("Key not found.")

print(my_dict)
