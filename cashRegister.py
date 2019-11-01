price = 0
given = 0
change = 0
dollar = 0
halfDollar = 0
quarter = 0
dime = 0
nickel = 0
penny = 0

price float(input("What is the price?: $"))
given float(input("Waht is the given money?: $"))

halfDollar += dollar * 2
quarter += halfDollar * 2
dime += quarter * 2.5
nickel += dime * 2
penny += nickel * 5

while penny >= 0:

	nickel = int(penny / 100)
	penny = penny % 100

	dime = int(nickel / 100)
	nickel = nickel % 100

	quarter = int(dime / 100)
	dime = dime % 100

	halfDollar = int(quarter / 100)
	quarter = quarter % 100

	dollar = int(halfDollar / 100)
	halfDollar = halfDollar % 100

	print("Dollar: $ " + dollar)
	print("HalfDollar: $" + halfDollar)
	print("Quarter: $" + quarter)
	print("Dime: $" + Dime)
	print("Nickel: $" + Nickel)
	

