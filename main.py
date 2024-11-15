def main():
	with open("books/frankenstein.txt") as f:
		file_contents = f.read()
	
	#Word Count
	wordCount=file_contents.split()
	print(f"{len(wordCount)} words found in document")

	#Character Count
	characterDict={}
	for character in file_contents.lower():
		if character.isalpha()==True:
			if character in characterDict:
				characterDict[character]+=1
			else:
				characterDict[character]=1

	for char, count in characterDict.items():
		print(f"The {char} character was found {count} times.")


main()