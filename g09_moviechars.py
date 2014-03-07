import re

filename = input("Enter name of the text file: ")
f = open(filename, 'r')
text = f.read()
words = set(text.split())
caps = set()

punctuation = [',', '.', '\'', '\"', '!', '?', '...', ':']

for word in words:
	if (word[0].isupper()): 
		if (word[-3:] in punctuation):
			word = word[:-3]
		if(word[-1] in punctuation):
			word = word[:-1]

		caps.add(word)
capsstart = set(re.findall('\.\s+([A-Za-z]+)', text))
capsnotstart = caps - capsstart


