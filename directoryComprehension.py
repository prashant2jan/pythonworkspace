sentence = "the quick brown fox jumps over the lazy dog"
word_counts = {word: sentence.split().count(word) for word in 
               set(sentence.split())}
print(word_counts)

from collections import Counter
word_counts = Counter(sentence.split())
print(word_counts)