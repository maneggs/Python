import random

listvalues = []

for negval in range(1, random.randint(2, 10)):
    negativerandvalues = random.randint(-1000, -1)
    listvalues.append(negativerandvalues)

for posval in range(1, random.randint(2, 10)):
    positiverandvalues = random.randint(1, 1000)
    listvalues.append(positiverandvalues)

for zero in range(0, random.randint(0, 1)):
    listvalues.append(0)

print(f"Минимальное: {min(listvalues)}")
print(f"Maксимальное: {max(listvalues)}")

negativenumbers = []
positivenumbers = []

for number in listvalues:
    if number < 0:
        negativenumbers.append(number)
    elif number > 0:
    	positivenumbers.append(number)

print("\nНегативные числа: ")
for i in negativenumbers:
	print(i)

print("\nПозитивные числа: ")
for e in positivenumbers:
	print(e)

zero = listvalues.count(0)
print(f"\nНули: {zero}")

input("")