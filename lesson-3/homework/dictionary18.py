from collections import defaultdict

# Creating a defaultdict with a default value of 0 for missing keys
my_dict = defaultdict(int)

# Adding some data
my_dict['a'] = 5
my_dict['b'] = 10

# Accessing existing keys
print(my_dict['a'])  # Output: 5
print(my_dict['b'])  # Output: 10

# Accessing a missing key
print(my_dict['c'])  # Output: 0 (default value)
