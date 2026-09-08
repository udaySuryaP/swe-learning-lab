limitValue = int(input("Enter the maximum value: "))
oddList = []

for i in range(limitValue):
    if (i % 2 != 0):
        oddList += [i]

print(oddList)
