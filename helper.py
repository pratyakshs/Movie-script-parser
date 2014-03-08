import re
import operator

filename = input("Enter name of the text file: ")
f = open(filename, 'r')
text = f.read()
words = set(text.split())
caps = set()

punctuation = [',', '.', '\'', '\"', '!', '?', '...', ':', ')', '(', '[', ']', '&']

#for word in words: 
#	if (word[-3:] in punctuation):  # words ending with ...
#		word = word[:-3]
#	if(word[-1] in punctuation):	# words ending with punctuation
#		word = word[:-1]
#	caps.add(word)

#capsstart = set(re.findall('\.\s+([A-Za-z]+)', text))
#capsnotstart = caps - capsstart

dictfile = open('/usr/share/dict/words', 'r')
dictwords = dictfile.read().splitlines()

x = set()
for w in words:
	if (w.lower() in dictwords):
		x.add(w)

char_counts = dict()			   
for word in x:
	if (len(word)>4) and (text.count(word) >= 5):
		char_counts[word] = text.count(word)
	
sorted_list = sorted(char_counts.items(), key = lambda char_counts: -char_counts[1])

