#Declare variables

budget = 500
economy = 750
vip = 2000
bag = 200
meal = 150

bag_count = 0
meal_count = 0

max_bags = 1
max_meals = 1

chosenTicket = None

#Starting point to print the options available

startingPoint = "Ticket types:\n1. Budget  ( " + str(budget) + "kr)\n2. Economy ( " + str(economy) + "kr)\n3. VIP     (" + str(vip) + "kr)\n"

print(startingPoint)

#While statement to make sure the input is a valid option

while True:

  ticket = input('Input ticket type >> ')

  if not ticket.isdigit() or not 1 <= int(ticket) <= 3:
    print("\nInvalid choice\n")  
    print(startingPoint)
  else:
    ticket = int(ticket)
    break

if ticket == 1:
  chosenTicket = budget

if ticket == 2:
  chosenTicket = economy

if ticket == 3:
  chosenTicket = vip

#Print the current selection of bags and meals and second selection menu

print("\nCurrently you have:\n\t" + str(bag_count) + " bag(s) registered\n\t" + str(meal_count) + " meal(s) registered\n")

secondSelection = "Here are your options:\n1. Add bag (max 1)\n2. Add meal (max 1)\n3. Remove bag\n4. Remove meal\n5. Finalize ticket\n"

print(secondSelection)

#Implementation of second selection menu, in a while loop to make sure all entered numbers are valid. There are also checks to make sure bags or meals can't be higher than the allowed value or go to negative values.

while True:

  bagMealSelection = input("Your choice >> ")

  if not bagMealSelection.isdigit() or not 1 <= int(bagMealSelection) <= 5:
    print("\nInvalid choice\n")  
    print(secondSelection)
  else:    
    bagMealSelection = int(bagMealSelection)

    if bagMealSelection == 1:
      bag_count += 1
      print("\nCurrently you have:\n\t" + str(bag_count) + " bag(s) registered\n\t" + str(meal_count) + " meal(s) registered\n")
      print(secondSelection)
      if bag_count > max_bags:
        print("Too many bags! Please remove a bag.\n")

    elif bagMealSelection == 2:
      meal_count += 1
      print("\nCurrently you have:\n\t" + str(bag_count) + " bag(s) registered\n\t" + str(meal_count) + " meal(s) registered\n")
      print(secondSelection)
      if meal_count > max_meals:
        print("Too many meals! Please remove a meal\n")

    elif bagMealSelection == 3:
      bag_count -= 1
      if bag_count < 0:
        bag_count = 0
      print("\nCurrently you have:\n\t" + str(bag_count) + " bag(s) registered\n\t" + str(meal_count) + " meal(s) registered\n")
      print(secondSelection)

    elif bagMealSelection == 4:
      meal_count -=1
      if meal_count < 0:
        meal_count = 0
      print("\nCurrently you have:\n\t" + str(bag_count) + " bag(s) registered\n\t" + str(meal_count) + " meal(s) registered\n")
      print(secondSelection)
    
    elif bagMealSelection == 5:
      if bag_count > max_bags:
        print("\nToo many bags! Please remove a bag.\n")

      elif meal_count > max_meals:
        print("\nToo many meals! Please remove a meal\n")
      else:
        break

totalBagPrice = bag_count * bag
totalMealPrice = meal_count * meal
totalPrice = chosenTicket + totalBagPrice + totalMealPrice

print("Receipt:")
print("Ticket : " + format(chosenTicket, ">4") + "kr")
print("Bag    : " + format(bag_count * bag, ">4") + "kr")
print("Meal   : " + format(meal_count * meal, ">4") + "kr")
print("        -------")
print("Total  : " + format(totalPrice, ">4") + "kr")
