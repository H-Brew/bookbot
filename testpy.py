emptyDict={}

letters = ('a','b','a','d','c','a','b','e')

for letter in letters:
	if letter in emptyDict:
		emptyDict[letter]+=1
	else:
		emptyDict[letter]=1

for val in emptyDict:
	print(emptyDict[val])
