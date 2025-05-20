import os
import string 
from collections import Counter
#checking if the file exists
if not os.path.exists("sample.txt"):
    user_input = input("Write a text to use: ")
    with open("sample.txt", "w") as file:
        file.write(user_input)
#reading data
with open("sample.txt", "r") as file:
        content = file.read()

cleaned_text = "".join([char for char in content if char not in string.punctuation]).lower()
words = cleaned_text.split()
word_counts = Counter(words)
while True:
     try:
        top_n = int(input("How many top common words do you want to display: "))
        break
     except ValueError:
          print("Please enter a valid number: ")
total_words = sum(word_counts.values())
print(f"\nTotal words: {total_words}")
print(f"Top {top_n} most common words:")
for word, count in word_counts.most_common(top_n):
     print(f"{word} - {count} time{'s' if count > 1 else ''}")

with open("word_count_report.txt", "w") as report:
     report.write("Word count report\n")
     report.write(f"Total Words: {total_words}\n")
     report.write(f"Top {top_n} Words:\n")
     for word, count in word_counts.most_common(top_n):
          report.write(f"{word} - {count}\n")
print("Results have been saved to 'word_count_report.txt'")