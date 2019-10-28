myWord = "panda"
myList = list("_____")


while True:
	choice = input("Type a word: ")

	if choice == myWord:
		print("That is the correct Word")
		print("Congrats, You Win!")
		break
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

	if letter == myWord:
		print(Correct)

	count = 1
	for p in myWord:
		if p == letter:
			print(count)
		count += 1

	if choice == "end":
		break