list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

uncommon_list = []
for item in list1:
   if item not in list2:
      uncommon_list.append(item)

for item in list2:
   if item not in list1:
      uncommon_list.append(item)
print(uncommon_list)