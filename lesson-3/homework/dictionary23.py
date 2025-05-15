dict1 = {'name': 'Mohina', 'age': 18, 'major': 'AI & Robotics'}
dict2 = {'university': 'New Uzbekistan University', 'age': 19, 'city': 'Tashkent'}
common_keys = set(dict1.keys()) & set(dict2.keys())

print(common_keys)
