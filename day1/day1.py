def menu():
    print("Day 1")

def openFile():
    try:
        with open("day1.txt", "r") as data:
            document = data.readlines()
            return document
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print(f"Problem with reading file: {e}")
        return None

def calibration(data):
    sum = 0

    try:
        for line in data:
            line = line.rstrip()

            if line and any(char.isdigit() for char in line):
                firstDigit = next(char for char in line if char.isdigit())
                lastDigit = next(char for char in reversed(line) if char.isdigit())

                value = int(firstDigit + lastDigit)
                sum += value

        return sum

    except Exception as e:
        print(f"Error during reading data: {e}")
        return None


def main():
    menu()
    data = openFile()

    if data is not None:
        value = calibration(data)
        print("Total sum: ", value)


if __name__ == "__main__":
    main()
