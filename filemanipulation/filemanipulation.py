from collections import Counter
import string

def count_words(word_count):
    try:
        with open(word_count, 'r', encoding='utf-8') as file:
            text = file.read()
        
        text = text.translate(str.maketrans('', '', string.punctuation)).lower()
        words = text.split()
        
        word_counts = Counter(words)
        
        sorted_word_counts = sorted(word_counts.items())
        
        for word, count in sorted_word_counts:
            print(f"{word}: {count}")
    except FileNotFoundError:
        print("File not found. Please provide a valid filename.")

word_count = input("Enter the full file path: ").strip()
count_words(word_count)