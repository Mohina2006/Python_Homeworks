txt = input("Enter your text: ")
vowels = "aeiou"
used_items = set()
new_txt = []
i = 0
for j in range(len(txt)):
    new_txt.append(txt[j])
    i = i + 1
    if i >= 3 and txt[j] not in vowels and txt[j] not in used_items and j != len(txt) - 1:
        new_txt.append("_")
        used_items.add(txt[j])
        i = 0
    else:
        continue
print("".join(new_txt))