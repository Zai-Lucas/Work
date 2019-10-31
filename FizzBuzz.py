count = 1
while count <= 100:
	print(count, end="")
	if count % 3 == 0:
		print("-fizz", end="")
	if count % 5 == 0:
		print("-buzz", end="")
	count += 1
	print("")