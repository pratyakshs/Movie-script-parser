filename = input("Enter name of the text file: ")
f = open(filename, 'r')
line = f.readline()
while ("".join(line.split()) == ''):
	line = f.readline()
title = line.strip()
print(title)


line = f.readline()
while ("".join(line.split()) == ''):
	line = f.readline()

if (line.lstrip().rstrip() == 'Written by'):
#	print('Hello')
	line = f.readline()
	while (line == '\n'):
		line = f.readline()
author = line.strip()
line = f.readline()
while (line != '\n'):
	author = author + ',' + line.strip()
	line = f.readline()
#print(title)
print(author)
