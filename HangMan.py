myWord = list("panda")
myList = list("_____")


while True:
	choice = input("Type a word: ")

	if choice == myWord:
		print("That is the correct Word")
	else:
		print("that is not the Word")

	index = 0
	guess = input("Type a Letter: ")
	for letter in myWord:
		if letter == guess:
			myList[index] = guess
			print("That is a Letter")
		index += 1	
	else:
		print("That isn't a Letter")
	print(myList)

	count = 1
	for s in myWord:
		if s == letter:
			print(count)
		count += 1

	if choice == "end":
		break