import sys


def read_lines(filename):
    try:
        # Opens the file as read only
        with open(filename, 'r') as cars:
            # Gets all lines into a list
            listOfCars = cars.readlines()
            i = 0
            # Removes newline characters
            while i < len(listOfCars):
                listOfCars[i] = listOfCars[i].rstrip("\n")
                i += 1

    # Throws an exception if the file path is wrong
    except IOError:
        print("An error occurred while trying to read the file.")
        sys.exit()

    return listOfCars


# Takes a list of strings and converts it into a list of tuples
# each tuple has 2 values, that were separated by a ':'
# in the string
def parse_cars(list_of_strings):
    i = 0
    listOfTuples = []
    while i < len(list_of_strings):
        listOfTuples.append(list(list_of_strings[i].split(':')))
        listOfTuples[i][1] = int(listOfTuples[i][1])
        listOfTuples[i] = tuple(listOfTuples[i])
        i += 1

    return listOfTuples


# Takes the distance and the list of tuples
# and replaces the distance with the percentage
# of the user input for each car in the list
def calculate_percentage(distance, cars):
    percentages = []
    for item in cars:
        percentages.append(tuple((item[0],
                           float((int(distance) / int(item[1]) * 100)))))

    return percentages


# Prints the list with percentages
def display_result(percentages):
    print("To drive the specified distance would correspond to this many\n"
          "percent of each cars specified max range.")
    i = 0
    for item in percentages:
        if percentages[i][1] > 100:
            percent = int(round(percentages[i][1]))
            print(format(percentages[i][0], "<37")
                  + "-->  Distance exceeds max range ("
                  + str(percent) + "%)")

        else:
            print(format(percentages[i][0], "<37") + "-->  "
                  + str(round(percentages[i][1])) + "%")
        i += 1


def main():
    # Checks that the correct amount of arguemnts are given
    if len(sys.argv) == 2:
        # Gets the list of tuples from the read_lines function
        listOfCars = read_lines(sys.argv[1])
        # Calls parse_cars to get a list of tuples
        parsedList = parse_cars(listOfCars)
        # Asks the user how far to drive
        distance = input("How far do you want to drive (kilometers) >> ")
        # Converts the distances to percentages based on user input
        percentages = calculate_percentage(distance, parsedList)
        # Displays the result
        display_result(percentages)

    else:
        print("Too few or too many arguments were given.")


main()
