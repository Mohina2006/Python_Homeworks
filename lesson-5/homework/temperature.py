def convert_cel_to_far(C):
    fahrenheit = C * 9 / 5 + 32
    return f"{C} degrees C = {fahrenheit:.2f} degrees F"

def convert_far_to_cel(F):
    celcius = (F - 32) * 5/9
    return f"{F} degress F = {celcius:.2f} degress C"


user_input1 = float(input("Enter a temperature in degrees F: "))
func2 = convert_far_to_cel(user_input1)
print(func2)

user_input = float(input("Enter a temperature in degrees C: "))
func1 = convert_cel_to_far(user_input)
print(func1)