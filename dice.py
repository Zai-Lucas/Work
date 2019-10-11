# Name: Isaiah Lucas
# 6 Period 
# Dice Rolling Simulator
import random 
random.randint(1, 6)

numOne = 0
numTwo = 0
numThree = 0
numFour = 0
numFive = 0
numSix = 0

def printNum(): #displays number of specific number
	print("1s: " + str(numOne))
	print("2s: " + str(numTwo))
	print("3s: " + str(numThree))
	print("4s: " + str(numFour))
	print("5s: " + str(numFive))
	print("6s: " + str(numSix))

def printPercent(): #display percent of specific number
	print("1s: " + str(numOne / 100 * 100) + "%")
	print("2s: " + str(numTwo / 100 * 100) + "%")
	print("3s: " + str(numThree / 100 * 100) + "%")
	print("4s: " + str(numFour / 100 * 100) + "%")
	print("5s: " + str(numFive / 100 * 100) + "%")
	print("6s: " + str(numSix / 100 * 100) + "%")

rolls = int(input("how many rolls "))
x = 1
while x <= rolls:
	x += 1
	RandNum = random.randint(1,6)
	print(RandNum) #counts number
	if RandNum == 1:
		numOne += 1
	if RandNum == 2:
		numTwo += 1
	if RandNum == 3:
		numThree += 1
	if RandNum == 4:
		numFour += 1
	if RandNum == 5:
		numFive += 1
	if RandNum == 6:
		numSix += 1
	

printNum()
printPercent()