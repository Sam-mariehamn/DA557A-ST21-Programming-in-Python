# Declare the variables

start = 72
exit = 18
power = [14, 68]
trap = [16, 29, 93]
wall = [
  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 17, 19, 23, 24, 26,
  27, 31, 37, 39, 41, 43, 44, 45, 47, 51, 53, 55, 57,
  58, 61, 63, 65, 67, 71, 75, 77, 78, 81, 82, 83, 84,
  85, 94, 95, 96, 97, 98, 99
  ]

moves = 20
currentSquare = 0
text = ""
allowedMoves = ["w", "a", "s", "d"]
status = False
temp = ""
isPower = False
isTrap = False

# A function to check if the move ran into a wall/trap/powerup


def result(value):

    for i in range(len(power)):
        if value == power[i]:
            global moves
            global isPower
            moves += 15
            text = "A chocolate bar, I feel stronger."
            isPower = True
            return text

    for i in range(len(trap)):
        if value == trap[i]:
            global currentSquare
            global isTrap
            currentSquare = start
            text = "Oh no, a trap!"
            isTrap = True
            return text

    for i in range(len(wall)):
        if value == wall[i]:
            text = "Ouch! I can not walk through walls…"
            return text


# Initiate the current square to be the starting square and print
# the starting message

print("\nYou have been placed in a pitch-black labyrinth, without knowing "
      "if there is a way out or not. Maybe there are traps? "
      "The only option available is to walk in a random direction "
      "and hope for the best, hope that you do not walk into a wall, "
      "or even worse, that you walk in circles. But hurry up, "
      "you only have so many moves…\n\nTo move around use:"
      "\nw - up\na - left\ns - down\nd - right\n")

currentSquare = start

# While loop until moves = 0 or exit is found.

while True:
    print(currentSquare)
    direction = input("Enter direction >> ")
    direction = direction.lower()

    # A for loop to check if the input is allowed
    for i in range(len(allowedMoves)):
        if direction == allowedMoves[i]:
            status = True

    if status:

        # Set status to false so this block doesn't run again if the
        # input is invalid
        status = False

        if direction == "w":
            # Check to see if the move goes outside the labyrinth
            if currentSquare - 10 < 0:
                print("Ouch! I can not walk through walls…")
            else:
                # Temp variable used so that the function doesn't run twice
                # in case of power
                temp = result(currentSquare - 10)
                if temp is None:
                    currentSquare -= 10
                    moves -= 1
                else:
                    print(temp)
                    # isPower variable is so that the move is registered if
                    # we power up. That is not needed for wall or trap.
                    if isPower:
                        currentSquare -= 10
                        # Set isPower to false so that it doesn't run again
                        # unless the square is a powerup.
                        isPower = False
                        moves -= 1
                    if isTrap:
                        isTrap = False
                        moves -= 1

        if direction == "a":
            if(currentSquare - 1) % 10 == 9:
                print("Ouch! I can not walk through walls…")
            else:
                temp = result(currentSquare - 1)
                if temp is None:
                    currentSquare -= 1
                    moves -= 1
                else:
                    print(temp)
                    if isPower:
                        currentSquare -= 1
                        isPower = False
                        moves -= 1
                    if isTrap:
                        isTrap = False
                        moves -= 1

        if direction == "s":
            if currentSquare + 10 > 99:
                print("Ouch! I can not walk through walls…")
            else:
                temp = result(currentSquare + 10)
                if temp is None:
                    currentSquare += 10
                    moves -= 1
                else:
                    print(temp)
                    if isPower:
                        currentSquare += 10
                        isPower = False
                        moves -= 1
                    if isTrap:
                        isTrap = False
                        moves -= 1

        if direction == "d":
            if (currentSquare + 1) % 10 == 0:
                print("Ouch! I can not walk through walls…")
            else:
                temp = result(currentSquare + 1)
                if temp is None:
                    currentSquare += 1
                    moves -= 1
                else:
                    print(temp)
                    if isPower:
                        currentSquare += 1
                        isPower = False
                        moves -= 1
                    if isTrap:
                        isTrap = False
                        moves -= 1

    else:
        print("Invalid move, try again!")

    # Check for exit before we check if we're out of
    # moves as we can still make it on the last move.
    if currentSquare == exit:
        print("You survived! Well done adventurer!")
        break

    if moves == 0:
        print("Game over! You did not reach the exit in time.")
        break
