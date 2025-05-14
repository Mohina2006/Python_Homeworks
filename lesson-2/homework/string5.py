text = input("Enter a simple text: ")
text = text.lower()

only_letters = ''.join(filter(str.isalpha, text))

vowel_count = (
    only_letters.count('a') +
    only_letters.count('e') +
    only_letters.count('i') +
    only_letters.count('o') +
    only_letters.count('u')
)

consonants_count = len(only_letters) - vowel_count

print(f"There are {vowel_count} vowels present")
print(f"There are {consonants_count} consonants present")
