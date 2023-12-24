import re

def menu():
    print("Day 4")

def openFile():
    try:
        with open("day4.txt", "r") as file:
            document = file.read().strip().split('\n')
            return document
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print(f"Problem with reading file: {e}")
        return None

def calculatePoints(data):
    sum = 0

    for value in data:
        parts = re.split(r'\s*[:|]\s*', value)

        if len(parts) >= 3:
            winNumbers = [int(x) for x in parts[1].split() if x != '']
            chosenNumbers = [int(x) for x in parts[2].split() if x != '']

            numbers = [x for x in chosenNumbers if x in winNumbers]

            if numbers:
                points = 2**(len(numbers) - 1)
                sum += points

    return sum

def main():
    menu()
    data = openFile()

    if data is not None:
        totalPoints = calculatePoints(data)
        print("Total points:", totalPoints)

if __name__ == "__main__":
    main()
