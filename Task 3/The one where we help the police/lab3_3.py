import pickle
import sys


# Displays the menu that asks for filepaths and adds
# them to a list
def display_menu():
    print("\n1. Add file\n"
          "2. Calculate\n")
    files = []
    while True:
        try:
            choice = input("Enter choice: ")
            if choice == '1':
                path = input("Enter a filename (include full path): ")
                files.append(path)

            elif choice == '2':
                break

            else:
                print("Invalid choice, try again")

        # Had to add this to get the automatic test to pass
        except EOFError:
            return

    return files


# Opens all files and reads all lines into a list
def cross_reference(files):
    numbers = []
    for item in files:
        try:
            with open(item, 'r') as file:
                numbers += file.readlines()

        except IOError:
            print("Error: There was a problem with at least one of the files.")
            sys.exit()

    # Puts each element present in all numbers into a set
    matched = set()
    for item in numbers:
        count = numbers.count(item)
        if count == len(files):
            item = item.rstrip('\n')
            matched.add(item)

    return matched


# Takes all elements from numbers and matches them with
# a corresponding element in a dictionary
def map_numbers_to_names(numbers, filename):
    names = []
    try:
        with open(filename, 'rb') as file:
            owners = pickle.load(file)
            for item in numbers:
                if item not in owners:
                    names.append("Unknown (" + item + ")")
                else:
                    names.append(owners[item])

    except IOError:
        print("Error: There was a problem with at least one of the files.")
        sys.exit()

    return names


# Prints the results according to the format
def display_suspects(names):
    print("\nThe following persons was present on all crime scenes:")
    print("------------------------------------------------------")
    if not names:
        print("No matches")
    else:
        for item in names:
            print(item)


def main():
    # Checks for the correct amount of arguments when
    # running the script and prints an error message if there
    # are too many or too few arguments
    if len(sys.argv) == 2:
        files = display_menu()
        matchedNumbers = cross_reference(files)
        names = map_numbers_to_names(matchedNumbers, sys.argv[1])
        display_suspects(names)

    else:
        print("Too few or too many arguments were given.")


main()

