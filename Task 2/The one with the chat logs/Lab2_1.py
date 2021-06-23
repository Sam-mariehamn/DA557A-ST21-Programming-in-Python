import sys

def read_file(filename):

    try: 
        with open(filename, 'r') as chatLog:
            chatLogList = chatLog.readlines()
            i = 0
            while i < len(chatLogList):
                chatLogList[i] = chatLogList[i].rstrip("\n")
                i += 1
            it = iter(chatLogList)
            listOfTuples = list(zip(it, it))

    except IOError: 
        print("The file " + filename + " could not be found.")

    return listOfTuples



def display_entry(name, message):
    print("[" + name + "] --> " + message)



def main():

    if len(sys.argv) == 2:
        name = input("Enter a name to search for >>")        
        listOfTuples = read_file(sys.argv[1])
        for item in listOfTuples:
            if item[0] == name:
                display_entry(name, item[1])

    else:
        print("Too few or too many arguments were given.")


main()
