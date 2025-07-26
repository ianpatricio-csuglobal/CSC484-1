"""
Title: State of the Union Speech Analyzer
Description: This Python script reads a speech from a text file and performs
             statistical analysis including word count, character count,
             average word and sentence lengths, word frequency distribution,
             and the longest words used in the speech.

Author: Ian Patricio
Date: July 26, 2025
"""
import re
from collections import Counter
from tabulate import tabulate

# Load the speech from a file
file_path = "state_of_the_union.txt"  # Replace with your actual path if needed
with open(file_path, "r", encoding="utf-8") as file:
    speech = file.read()

# Sentence and word tokenization
sentences = re.split(r'[.!?]+', speech)
words = re.findall(r'\b\w+\b', speech)

# Basic statistics
word_count = len(words)
char_count = len(speech)
avg_word_len = sum(len(word) for word in words) / word_count
avg_sent_len = word_count / len(sentences)

# Word frequency (case insensitive)
word_freq = Counter(map(str.lower, words))
most_common_words = word_freq.most_common(10)

# Top 10 longest unique words
unique_words = set(words)
longest_words = sorted(unique_words, key=len, reverse=True)[:10]

# Summary table
summary_table = [
    ["Word Count", word_count],
    ["Character Count", char_count],
    ["Average Word Length", f"{avg_word_len:.2f}"],
    ["Average Sentence Length (words)", f"{avg_sent_len:.2f}"],
    ["Top 10 Longest Words", ", ".join(longest_words)],
]

# Display summary
print("\nSpeech Summary:")
print(tabulate(summary_table, headers=["Metric", "Value"], tablefmt="fancy_grid"))

# Display word frequency
print("\nWord Frequency Distribution (Top 10 Words):")
print(tabulate(most_common_words, headers=["Word", "Frequency"], tablefmt="grid"))
