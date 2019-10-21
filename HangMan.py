myWord = "Panda"

while True:
	choice = input("Type a word: ")

	if choice == myWord:
		print("That is the correct Word")
	else:
		print("that is not the Word")


	letter = input("Type a Letter: ")
	if letter in myWord:
		print("That is a Letter")
	else:
		print("Not a Letter in the Word")

	count = 1
	for s in myWord:
		if s == letter:
			print(count)
		count += 1