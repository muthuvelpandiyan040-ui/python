
from collections import Counter
import string

try:
    # Open the text file
    with open("sample.txt", "r") as file:

        text = file.read()

    # 1. Count number of lines
    lines = text.splitlines()
    line_count = len(lines)

    # 2. Count number of words
    words = text.split()
    word_count = len(words)

    # 3. Count number of characters
    char_count = len(text)

    print("Number of Lines:", line_count)
    print("Number of Words:", word_count)
    print("Number of Characters:", char_count)

    # 4. Find top 5 most frequent words
    cleaned_words = []

    for word in words:
        word = word.lower()
        word = word.strip(string.punctuation)

        if word:
            cleaned_words.append(word)

    frequency = Counter(cleaned_words)

    print("\nTop 5 Most Frequent Words:")

    for word, count in frequency.most_common(5):
        print(word, ":", count)

except FileNotFoundError:
    print("Error: File not found!")

except PermissionError:
    print("Error: Permission denied!")

except Exception as e:
    print("An error occurred:", e)
