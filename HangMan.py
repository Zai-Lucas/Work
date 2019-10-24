myWord = "panda"
myList = list(myWord)
secret = []

for p in myList:
	secret.append("_")

secret[0] = "p"
secret[1] = "a"
secret[4] = "a"
secret[2] = "n"
secret[3] = "d"
print(secret)




while True:
	choice = input("Type a word: ")

	if choice == myWord:
		print("That is the correct Word")
	else:
		print("that is not the Word")


	letter = input("Type a Letter: ")
	if letter in my:
		print("That is a Letter")
	else:
		print("Not a Letter in the Word")

	count = 1
	for s in myWord:
		if s == letter:
			print(count)
		count += 1

	if choice == "end":
		break