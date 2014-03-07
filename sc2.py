def rm_spaces_h ( str2 ):
	for i in range(0,len(str2)):
		if(str2[i]!= ' '):
			return str2[i:]
def rm_spaces ( str2 ):
	str1=rm_spaces_h(str2)
	for i in range(0,len(str1)):
        	if(str1[len(str1) - i-1]!= ' '):
        		return str1[:len(str1)-i]

f=open('tdkr.txt','r')
words = set(f.read().split())
capital = set()
chars = set()
chars2 = set()
#for word in words:
#	if(word[0].isupper()):
#		if(word[-2:] != '\'s'):
#			capital.add(word)
#print (len(capital))
f=open('lm.txt','r')
lines = f.read().splitlines()
for line in lines:
	if(line[:26] == '                          ') and (line[26]!='(') and (line.isupper()) and line[-8:]!='(CONT\'D)':
		chars.add(rm_spaces (line))
		chars2.add(line)
print(chars)
print(len(chars))
#print(chars2)
#print(len(chars2))
