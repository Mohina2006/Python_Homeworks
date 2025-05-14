text = input("Enter a text:")
replace = input("Enter a word to replace:")
replace_with = input("Enter a word to replace with:")
start_index = text.find(replace)
if start_index != -1:
    end_index = start_index + len(replace)
    modified_text = text[:start_index] + replace_with + text[end_index:]
else:
    modified_text = text 

print(f"Modified text: {modified_text}")
