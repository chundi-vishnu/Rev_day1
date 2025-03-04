import re

def count_word_frequency(text):
    text=re.sub(r'[^A-Za-z0-9 ]+', '', text)
    words = text.split()
    word_freq = {}
    for word in words:
        word_freq[word] = word_freq.get(word,0) + 1
    return word_freq
text = input("Enter a text string: ").lower()
word_frequencies = count_word_frequency(text)
print("Word Frequencies:", word_frequencies)