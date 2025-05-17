def factors(a):
    factor_list = []
    for i in range(1, a + 1):
        if a % i == 0:
            factor_list.append(i)
    return factor_list

user_input = int(input("Enter a positive integer: "))
result = factors(user_input)
for f in result:
    print(f"{f} is a factor of {user_input}")
