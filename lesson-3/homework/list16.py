my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

odd_count = sum(num % 2 != 0 for num in my_list)
print(odd_count)