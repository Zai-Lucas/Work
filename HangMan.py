myWord = "panda"
myList = list("_____")
Miss = ("b""c""e""f""g""h""i""j""k""l""m""n""o""q""r""s""t""u""v""w""x""y""z")
MissList = list("-----------------------")

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
	for letter in Miss:
		if letter == guess:
			MissList[index] = guess
			print("That isn't a Letter")
		index += 1	
	print(MissList)
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