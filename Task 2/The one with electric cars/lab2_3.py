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


def parse_cars(list_of_strings):
    i = 0
    listOfTuples = []
    while i < len(list_of_strings):
        listOfTuples.append(tuple(list_of_strings[i].split(':')))
        i += 1

    return listOfTuples
        

def calculate_percentage(distance, cars):
    percentages = []
    for item in cars:
        percentages.append(tuple((item[0],
        float((int(distance) / int(item[1])* 100)))))

    return percentages


def display_result(percentages):
    print("To drive the specified distance would correspond "
          "to this many percent of each cars specified max range.")
    i = 0
    for item in percentages:
        if percentages[i][1] > 100:
            percent = int(percentages[i][1])
            print(format(percentages[i][0], "<37") + "-->  Distance exceeds max range ("
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
        percentages = calculate_percentage(distance, parsedList)
        display_result(percentages)

    else:
        print("Too few or too many arguments were given.")


main()
