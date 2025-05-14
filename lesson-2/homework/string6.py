text1 = input("Enter the first text:")
text2 = input("Enter the second text:")

if len(text2) > len(text1):  
    if text1 in text2:  
        print(f"{text2} contains {text1}")
    else:
        print(f"{text2} doesn't contain {text1}")
else:  
    if text2 in text1:  
        print(f"{text1} contains {text2}")
    else:
        print(f"{text1} doesn't contain {text2}")
