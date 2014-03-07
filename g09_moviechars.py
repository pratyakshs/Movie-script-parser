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
		
gender = dict()
for char in charlist:
	m, f, p = 0, 0, 0 
	for i in range(len(lines)):
		srch = re.search(char, lines[i], re.I)
		if not srch:
			continue
		if srch.group().isupper():
			continue
		else:
			k, k_range = -1, 2
			while k + i + 1 < len(lines):
				k = k + 1
				m = m + len(re.findall("\s+he", lines[k+i], re.I)) + len(re.findall("\s+him", lines[k+i], re.I))
				f = f + len(re.findall("\s+she", lines[k+i], re.I)) + len(re.findall("\s+her", lines[k+i], re.I))
				if lines[k+i].isupper():
					break
				if k >= k_range:
					break
			k, k_range = -1, 4
			while k + i + 1 < len(lines):
				k = k + 1
				m1, m2, m3, m4 = re.search("\s+he", lines[k+i], re.I), re.search("\s+him", lines[k+i], re.I), re.search("\s+she", lines[k+i], re.I), re.search("\s+her", lines[k+i], re.I)
				if m1:
					if m2:
						mc = min(m1.span()[0], m2.span()[0])
					else:
						mc = m1.span()[0]
				else:
					mc = len(lines[k+i])
				if m3:
					if m4:
						fc = min(m3.span()[0], m4.span()[0])
					else:
						fc = m3.span()[0]
				else:
					fc = len(lines[k+i])
				if not(m1 or m2 or m3 or m4):
					continue
				else:
					if (mc < fc):
						p = 0
					else:
						p = 1
					break
				if lines[k+i].isupper():
					break
				if k >= k_range:
					break
	gender[char] = m, f, p

for char, g in gender.items():
	g_score = 2.1*g[1] - g[0]
	g_sum = g[1]+g[0]
	if g[2] == 0:
		g_score = g_score - g_sum/10
	else:
		g_score = g_score + g_sum/10
	if (g_sum == 0.0) or (0 == 1):
		print(char+" Undetermined")
	elif g_score > 0:
		print(char+" Female"+str(g[0])+","+str(g[1])+","+str(g[2])+","+str(g_score))
	else:
		print(char+" Male"+str(g[0])+","+str(g[1])+","+str(g[2])+","+str(g_score))



#for word in words:
#	if (word[0].isupper()): 
#		if (word[-3:] in punctuation):  # words ending with ...
#			word = word[:-3]
#		if(word[-1] in punctuation):	# words ending with punctuation
#			word = word[:-1]
#		caps.add(word)
#
##capsstart = set(re.findall('\.\s+([A-Za-z]+)', text))
##capsnotstart = caps - capsstart
#
#dictfile = open('/usr/share/dict/words', 'r')
#dictwords = dictfile.read().splitlines()
#
#x = set()
#for w in caps:
#	if (w.lower() in dictwords):
#		x.add(w)
#
#characters = caps - x
#
#x = set()
#for word in characters:
#	if (any([char in word for char in punctuation])): # remove words which have pos
#		x.add(word)
#
#characters = characters - x
#
#x = set()
#for word in characters:
#	if (not (word.isupper()) and (word.upper() in characters)): # remove multiple occurances of words in different case
#		x.add(word)
#characters = characters - x


# sorted_list = sorted(char_counts.items(), key = lambda char_counts: -char_counts[1]

