words = input("Enter words separated by spaces:").split()
separator = input("Enter a separator character (e.g., - or ,): ")

result = separator.join(words)
print(f"Joined string: {result}")
