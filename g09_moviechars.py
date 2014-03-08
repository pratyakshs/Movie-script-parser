import re
import operator

filename = input("Enter name of the text file: ")
f = open(filename, 'r')
text = f.read()
lines = text.splitlines()
characters = dict()
punctuation = [',', '.', '\'', '\"', '!', '?', '...', ':', ')', '(', '[', ']', '&']

for line in lines:
	line = line.strip()
	if (line.isupper()):
		s1 = re.search('EXT\.', line)
		s2 = re.search('INT\.', line)
		if (not (s1 or s2)):
			if line in characters:
				characters[line] = characters[line] + 1
			else:
				characters[line] = 1
	
temp = dict()
for char, count in characters.items():
	if ((count > 4) and (not any([c in char for c in punctuation]))):
		temp[char] = len(re.findall(char, text, re.I))
characters = temp.copy()
del temp

charlist = sorted(characters)
for char in charlist:
	print(char+" "+str(characters[char]))
		
