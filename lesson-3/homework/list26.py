my_list = [10, 15, 20, 25, 30, 35, 40,50]
length = len(my_list)
if (length % 2 != 0):
    count1 = my_list[int(length/2)]
    print(count1)
else:
    count1 = my_list[int(length/2 - 1)]
    count2 = my_list[int(length/2)]
    print(count1, count2)