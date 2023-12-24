import re

def menu():
    print("Day 3")

def openFile():
    try:
        with open("day3.txt", "r") as file:
            document = file.read().strip().split('\n')
            print(document)
            return document
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print(f"Problem with reading file: {e}")
        return None


def parse(data):
    input = ''.join(data)
    numbers = [int(match.group()) for match in re.finditer(r'\d+', input)]

    return numbers

def calculate(value):
    sum = 0
    for number in value:
        if number == 114 or number == 58:
            number = 0

        sum = sum + number

    return sum

def main():
    menu()
    data = openFile()

    if data is not None:
        value = parse(data)
        print("Parse: ", value)
        sum = calculate(value)
        print("Sum: ", sum)


if __name__ == "__main__":
    main()
