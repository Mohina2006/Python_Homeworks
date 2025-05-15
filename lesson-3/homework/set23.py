import random
num_elements = 5        
min_value = 1          
max_value = 20          
random_set = set(random.sample(range(min_value, max_value + 1), num_elements))

print(random_set)
