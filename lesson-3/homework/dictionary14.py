my_dict = {'student1': "AI", "student2": "AI", "student3": "AI", "student4": "Applied Math"}
value = "AI"
my_list = []

for key, val in my_dict.items():
    if val == value:
        my_list.append(key)

print(my_list)
