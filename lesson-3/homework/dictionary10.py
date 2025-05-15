my_dict = {'name': "Mohina", 'age': 18, 'university': "New Uzbekistan University"}
key_to_find = 'university'

if key_to_find in my_dict:
    print(f"{key_to_find}: {my_dict[key_to_find]}")
else:
    print("Key not found.")
