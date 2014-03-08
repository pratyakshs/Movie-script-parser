import re
import operator
import math

### Code for identifying characters
filename = input("Enter name of the text file: ")
f = open(filename, 'r')
text = f.read()
lines = text.splitlines()
characters = dict()
punctuation = [',', '.', '\'', '\"', '!', '?', '...', ':', ')', '(', '[', ']', '&']

chars_inorder = [] 

for line in lines:
	line = line.strip()
	if (line.isupper()):
		s1 = re.search('EXT\.', line)
		s2 = re.search('INT\.', line)
		if (not (s1 or s2)):
			fi = line.find('(')
			if (fi != -1):
				line = line[:line.find('(')]
			line = line.strip()
			if (len(line) > 12):
				continue
			chars_inorder.append(line)
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

# to remove outliers
mean = 0
for i, j in characters.items():
	mean = mean + j
mean = mean / len(characters)

stddev = 0
for i, j in characters.items():
	stddev = stddev + (j - mean)*(j - mean)
stddev = stddev / len(characters)
stddev = math.sqrt(stddev)

temp = {}
for i, j in characters.items():
	if (math.fabs(j - mean) < 3*stddev):
		temp[i] = j
characters = temp.copy()
del temp

### Code for gender algorithm
charlist = sorted(characters)
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
						p = p - 1
					else:
						p = p + 1
					break
				if lines[k+i].isupper():
					break
				if k >= k_range:
					break
	gender[char] = m, f, p

for char, g in gender.items():
	g_score = 2*g[1] - g[0] 
	g_sum = g[1]+g[0]
	g_score = g_score
	if (g_sum == 0.0) or (0 == 1):
		print(char+" Undetermined ")
		gender[char] = 0, 0, -1
	elif g_score > 0:
		print(char+" Female "+str(g[0])+","+str(g[1])+","+str(g[2])+","+str(g_score))
		gender[char] = 0, 0, 1
	else:
		print(char+" Male", " ", str(g[0])+","+str(g[1])+","+str(g[2])+","+str(g_score))
		gender[char] = 0, 0, 0

# gender[char][2] = -1 if undetermined, 1 if female, 0 if male
	
charcount_sorted = sorted(characters.items(), key = lambda x: x[1], reverse = True)

for i in charcount_sorted:
	if (gender[i[0]][2] == 1):
		heroine = i[0]
		break

main_actors = charcount_sorted[:5]
main_actors = []
for i in charcount_sorted:
	if (len(main_actors) >= 5):
		break
	if (gender[i[0]][2] == 0):
		main_actors.append(i)

secondhalf_text = text[int(len(text)/2):]
secondhalf_count = {}
for char in main_actors:
	secondhalf_count[char[0]] = len(re.findall(char[0], secondhalf_text, re.I))

secondhalf_sorted = sorted(secondhalf_count.items(), key = lambda x: x[1], reverse = True)

freq_wt = {} # for villain
for k, char in enumerate(secondhalf_count):
	freq_wt[char] = [i for i, v in enumerate(main_actors) if v[0] == secondhalf_sorted[k][0]][0] - k


heroine_wt = {}
for i in main_actors:
	heroine_wt[i[0]] = 0

for index in [i for i, v in enumerate(chars_inorder) if v == heroine]:
	next_char = chars_inorder[index + 1]
	if (next_char in heroine_wt):
		prev = heroine_wt[next_char]
		heroine_wt[next_char] = prev + 1

heroine_wt = sorted(heroine_wt.items(), key = lambda x: x[1], reverse = False)

hero_score = {}
for i, char in enumerate(heroine_wt):
	hero_score[char[0]] = i
for i, char in enumerate(main_actors):
	hero_score[char[0]] = hero_score[char[0]] - i


hero = max(hero_score.keys(), key=(lambda key: hero_score[key]))

villain_score = -10
for i, j in freq_wt.items():
	if (i != hero):
		if (j > villain_score):
			villain = i
			villain_score = j

