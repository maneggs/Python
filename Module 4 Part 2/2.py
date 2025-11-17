listvalues = [-512, -12, 0, 1, 3, 7, 123, 6538, 63910, 991022, 9273514]

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