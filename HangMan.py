myWord = list("panda")
myList = list("_____")
index = 0




while True:
	choice = input("Type a word: ")

	if choice == myWord:
		print("That is the correct Word")
	else:
		print("that is not the Word")


	letter = input("Type a Letter: ")
	if letter == myWord:
		myList[index] = guess
		print("That is a Letter")
	index += 1	
	print(myList)

	count = 1
	for s in myWord:
		if s == letter:
			print(count)
		count += 1

	if choice == "end":
		break