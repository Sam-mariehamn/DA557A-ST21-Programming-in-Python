import sys

def read_file(filename):

    try: 
        # Opens the file as read only
        with open(filename, 'r') as chatLog:
            # Gets all lines into a list
            chatLogList = chatLog.readlines()
            i = 0
            # Removes newline characters
            while i < len(chatLogList):
                chatLogList[i] = chatLogList[i].rstrip("\n")
                i += 1
            # Converts the list into a list of tuples
            it = iter(chatLogList)
            listOfTuples = list(zip(it, it))
    # Throws an exception if the file path is wrong
    except IOError: 
        print("The file " + filename + " could not be found.")

    return listOfTuples


def display_entry(name, message):

    print("[" + name + "] --> " + message)


def main():
    # Checks that the correct amount of arguemnts are given
    if len(sys.argv) == 2:
        # Asks for whose messages to print
        name = input("Enter a name to search for >>")        
        # Gets the list of tuples from the read_file function
        listOfTuples = read_file(sys.argv[1])
        # Checks for all messages from the given name
        # and prints them 
        for item in listOfTuples:
            if item[0] == name:
                display_entry(name, item[1])
    
    else:
        print("Too few or too many arguments were given.")


main()
