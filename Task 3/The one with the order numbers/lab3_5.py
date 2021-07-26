import sys
import pickle


# Initiates the global variable to get letters
# from a number
TRANSLATION = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


# Loads the file and prints an error in case it fails
def read_orders(filename):
    try:
        with open(filename, 'rb') as file:
            orders = pickle.load(file)

    except IOError:
        print("Error: There was a problem with at least one of the files.")
        sys.exit()

    return orders


# Loads the file, strips the newline characters
# and prints an error in case it fails to read the file
def read_words(filename):
    try:
        with open(filename, 'r') as file:
            wordlist = file.readlines()
            i = 0
            while i < len(wordlist):
                wordlist[i] = wordlist[i].rstrip('\n')
                i += 1

    except IOError:
        print("Error: There was a problem with at least one of the files.")
        sys.exit()

    return wordlist


# Goes through all the numbers in the argument and calls add_digit for it
def find_all_possible_combinations(order_number):
    combinations = []
    for i in order_number:
        add_digit(i, combinations)
    return combinations


def add_digit(digit, combinations):
    # If the list is empty it adds all the letters for the digit
    if not combinations:
        for i in TRANSLATION[digit]:
            combinations.append(i)
    # If the list is not empty, removes the first entry of the list
    # and appends the removed entry plus the character from the digit
    # It does this for all characters from the digit
    else:
        for i in range(0, len(combinations)):
            n = combinations.pop(0)
            for j in TRANSLATION[digit]:
                combinations.append(n + j)

    return combinations


# Matches the entries from two lists using the fact that sets
# can only have unique entries
def filter_valid_words(possible_combinations, valid_words):
    words = list(set(possible_combinations).intersection(valid_words))
    return sorted(words)


# Formats and displays the result
def display_possible_words(order_number, words):
    for i in range(0, len(words)):
        if i == 0:
            print("\n" + order_number + " : " + words[i])

        else:
            print(format(words[i], ">" + str(len(order_number) * 2 + 3)))


def main():
    # Checks that the correct amount of arguemnts are given
    if len(sys.argv) == 3:
        orders = list(read_orders(sys.argv[1]))
        words = read_words(sys.argv[2])
        orders.sort()
        # Calls the functions for each order in the read list
        for i in orders:
            combinations = find_all_possible_combinations(i)
            possible_words = filter_valid_words(combinations, words)
            display_possible_words(i, possible_words)

    else:
        print("Too few or too many arguments were given.")


main()

