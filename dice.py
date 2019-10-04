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

def printNum():
	print("1s: " + str(numOne))

def printPercent():
	print("1s: " + str(numOne / 100) + "%")

rolls = int(input("how many rolls "))
x = 1
while x <= rolls:
	x += 1
	RandNum = random.randint(1,6)
	print(RandNum)
	if RandNum == 1:
		numOne += 1

printNum()
printPercent()
	

	