filename = input("Enter name of the text file: ")
f = open(filename, 'r')
data = set(f.read().split())
allcaps = set()
for word in data:
	if (word.isupper()): 
		allcaps.add(word)

