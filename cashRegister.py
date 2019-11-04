price = 0
given = 0
change = 0
dollar = 0
halfDollar = 0
quarter = 0
dime = 0
nickel = 0
penny = 0


price = float(input("What is the price?: $"))
given = float(input("Waht is the given money?: $"))
change = given - price
penny = change * 100


dollar = int(penny / 100)
penny = penny % 100

halfDollar = int(penny / 50)
penny = penny % 50

quarter = int(penny / 25)
penny = penny % 25

dime = int(penny / 10)
penny = penny % 10

nickel = int(penny / 5)
penny = penny % 5


print("Change: $" + str(change))
print("Dollar: " + str(dollar))
print("HalfDollar: " + str(halfDollar))
print("Quarter: " + str(quarter))
print("Dime: " + str(dime))
print("Nickel: " + str(nickel))
print("Penny: " + str(penny))