import sys


def read_file(filename):
    try:
        # Opens the file as read only
        with open(filename, 'r') as file:
            # Reads the lines and strips the newline character
            numbersAsString = file.readlines()
            i = 0
            while i < len(numbersAsString):
                numbersAsString[i] = numbersAsString[i].rstrip("\n")
                i += 1
            # Splits the numbers and puts them as integer into another
            # list that is returned
            numbers = []
            for item in numbersAsString:
                item = item.split(" ")
                for i in item:
                    numbers.append(int(i))

    except IOError:
        print("An error occurred while trying to read the file.")
        sys.exit()

    return numbers


# Gets all the odd or even numbers from the input list
# and puts them into another list that is returned
def filter_odd_or_even(numbers, odd):
    filtered = []
    if odd:
        for item in numbers:
            if item % 2 != 0:
                filtered.append(item)

    else:
        for item in numbers:
            if item % 2 == 0:
                filtered.append(item)

    return filtered


# Sorts the list in reverse order using Bubble Sort
def reversed_bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        for j in range(n-1):
            if numbers[j] < numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

    return numbers


def main():
    if len(sys.argv) == 3:
        list1 = read_file(sys.argv[1])
        list2 = read_file(sys.argv[2])

        odd = filter_odd_or_even(list1, True)
        even = filter_odd_or_even(list2, False)

        combined = odd + even

        sorted = reversed_bubble_sort(combined)

        print(sorted)

    else:
        print("Too few or too many arguments were given.")


main()

