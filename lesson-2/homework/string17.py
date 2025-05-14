text = input("Enter a string:")
vowels = "aeiou"

new_text = text
for vowel in vowels:
    new_text = new_text.replace(vowel, "*")

print(f"Updated string:{new_text}")