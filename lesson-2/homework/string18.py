text = input("Enter a string:")
start_word = input("Enter the word to check if the string starts with:")
end_word = input("Enter the word to check if the string ends with:")

if text.startswith(start_word) and text.endswith(end_word):
    print(f"The string starts with {start_word} and ends with {end_word}.")
else:
    print(f"The string does NOT start with {start_word} or end with {end_word}.")
