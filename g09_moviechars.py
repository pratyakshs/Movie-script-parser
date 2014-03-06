import re

filename = input("Enter name of the text file: ")
f = open(filename, 'r')
text = f.read()
words = set(text.split())
caps = set()

punctuation = [',', '.', '\'', '\"', '!', '?', '...', ':', ')', '(', '[', ']', '&']

for word in words:
	if (word[0].isupper()): 
		if (word[-3:] in punctuation):  # words ending with ...
			word = word[:-3]
		if(word[-1] in punctuation):	# words ending with punctuation
			word = word[:-1]
		caps.add(word)

#capsstart = set(re.findall('\.\s+([A-Za-z]+)', text))
#capsnotstart = caps - capsstart

dictfile = open('/usr/share/dict/words', 'r')
dictwords = dictfile.read().splitlines()

x = set()
for w in caps:
	if (w.lower() in dictwords):
		x.add(w)

characters = caps - x

x = set()
for word in characters:
	if (any([char in word for char in punctuation])):
		x.add(word)

characters = characters - x	
