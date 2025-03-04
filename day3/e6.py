text="the quick brown fox jumps overthe lazy dog"
word_count = {word: text.split().count(word) for word in set(text.split())}

# Print the word count dictionary
print(word_count)