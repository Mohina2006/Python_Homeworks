text = input("Enter a string:")
if (text.find('0') != -1 or
    text.find('1') != -1 or
    text.find('2') != -1 or
    text.find('3') != -1 or
    text.find('4') != -1 or
    text.find('5') != -1 or
    text.find('6') != -1 or
    text.find('7') != -1 or
    text.find('8') != -1 or
    text.find('9') != -1):
    print("The string contains digits.")
else:
    print("The string does not contain any digits.")