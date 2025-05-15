my_list = [10, 15, 20, 25, 30, 35, 40]

odd_numbers = list(filter(lambda num: num % 2 != 0, my_list))
print(odd_numbers)