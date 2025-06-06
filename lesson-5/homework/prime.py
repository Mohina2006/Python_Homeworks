import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):  
        if n % i == 0:
            return False
    return True

user_input = int(input("Enter the number to check if it is prime: "))
result = is_prime(user_input)
print(result)
