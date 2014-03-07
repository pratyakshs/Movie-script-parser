filename = input("Enter name of the text file: ")
f = open(filename, 'r')
text = f.read()
words = set(text.split())
words_mulset = text.split()

word_counts = dict()
for w in words:
	word_counts[w] = words_mulset.count(w)

import operator
sorted_words = sorted(word_counts.items(), key = lambda word_counts: word_counts[1])

