while True:
	primerchick = input("Введи выражение: ")

	if "+" in primerchick:
		a, b = primerchick.split("+")
		print(float(a)+float(b))

	elif "-" in primerchick:
		a, b = primerchick.split("-")
		print(float(a)-float(b))

	elif "*" in primerchick:
		a, b = primerchick.split("*")
		print(float(a)*float(b))

	elif "/" in primerchick:
		a, b = primerchick.split("/")
		print(float(a)/float(b))

	else:
		print(primerchick+" введен некорректно")

input("")