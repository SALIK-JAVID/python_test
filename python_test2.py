import re
from collections import Counter

def count_word_frequencies(text: str):
    # Convert text to lowercase and remove punctuation
    words = re.findall(r'\b[a-z]+\b', text.lower())
    
    # Count word occurrences
    word_counts = Counter(words)
    
    # Sort by frequency (descending) and then alphabetically
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Print results
    print("Word Frequencies:")
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")

# Example input
text = "Hello world! This is a test. Hello, this test is only a test."
count_word_frequencies(text)
