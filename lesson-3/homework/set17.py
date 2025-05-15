my_set = {1, 2, 3, 4, 5, 6}
odd_numbers = set(filter(lambda num : num % 2 != 0, my_set))
print(odd_numbers)