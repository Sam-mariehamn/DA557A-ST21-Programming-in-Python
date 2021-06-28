import pickle
import sys


def read_file(filename):
    try:
        with open(filename, 'rb') as file:
            content = pickle.load(file)

    except IOError:
        print("Error: The files given as arguments are not valid.")
        sys.exit()

    return content


def map_to_int(measurements):
    for key in measurements:
      measurements[key] = int(measurements[key].rstrip("°"))

    return measurements


def find_faulty(primary, secondary, threshold):
    faulty = set()
    for key in primary:
        if primary[key] > secondary[key]:
            difference = primary[key] - secondary[key]
        else:
            difference = secondary[key] - primary[key]

        if difference > threshold:
            faulty.add(key)

    return faulty


def display_warnings(faulty_sensors):
    print("Analyzis of the provided files is complete.\n"
          "-------------------------------------------\n"
          "The following sensors differ more than 2°:")
    for key in faulty_sensors:
        print(key)
    

def main():
    if len(sys.argv) == 3:
        dict1 = read_file(sys.argv[1])
        dict2 = read_file(sys.argv[2])

        mapped1 = map_to_int(dict1)
        mapped2 = map_to_int(dict2)

        faulty_sensors = find_faulty(mapped1, mapped2, 2)

        display_warnings(faulty_sensors)


    else:
        print("Too few or too many arguments were given.")

main()
