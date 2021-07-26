# Declare variables

bigCount = 0
mediumCount = 0
smallCount = 0

bigVolume = 80
mediumVolume = 50
smallVolume = 20

bigValue = 60000
mediumValue = 30000
smallValue = 10000

totalValue = 0

# Print welcome message

print("\nWelcome to the Money Bag Transport Calculator (M.B.T.C)")
print("-------------------------------------------------------\n")

# While loop to make sure we get a valid input from the user

while True:
    truckSize = input("What is the volume of the truck (>=100L) >> ")
    if not truckSize.isdigit() or int(truckSize) < 100:
        print("\nInvalid input, try again\n")
    else:
        truckSize = int(truckSize)
        break

# Calculate how many of each bag fits into
# the truck and the total value

while truckSize >= 80:
    bigCount += 1
    truckSize = truckSize - bigVolume

while truckSize >= 50:
    mediumCount += 1
    truckSize = truckSize - mediumVolume

while truckSize >= 20:
    smallCount += 1
    truckSize = truckSize - smallVolume

totalValue = (
                bigCount * bigValue
                + mediumCount * mediumValue
                + smallCount * smallValue
)

# Print the result

print("Packing plan")
print("------------")
print(str(bigCount) + " big bags")
print(str(mediumCount) + " medium bags")
print(str(smallCount) + " small bags\n")
print("Space left : " + str(truckSize) + "L")
print("Total value: " + str(totalValue) + "kr")
