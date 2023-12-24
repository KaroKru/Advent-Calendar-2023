import re
import math
from collections import defaultdict

def menu():
    print("Day 2")

def openFile():
    try:
        with open("day2.txt", "r") as data:
            document = data.readlines()
            return document
    except FileNotFoundError:
        print("File not found")
        return None
    except Exception as e:
        print(f"Problem with reading file: {e}")
        return None

def calculate(data, config):
    ids = 0
    sum = 0

    try:
        for record in data:
            recordedParts = re.sub("[;,:]", "", record).split()
            colormax = defaultdict(int)

            for count, color in zip(recordedParts[2::2], recordedParts[3::2]):
                colormax[color] = max(colormax[color], int(count))

            if colormax["red"] <= config["red"] and colormax["green"] <= config["green"] and colormax["blue"] <= config["blue"]:
                ids += int(recordedParts[1])

            sum += math.prod(colormax.values())

        return ids, sum

    except Exception as e:
        print(f"An error occurred during calculation: {e}")
        return None

def main():
    menu()
    data = openFile()
    config = {"red": 12, "green": 13, "blue": 14}

    if data is not None:
        ids, sum = calculate(data, config)
        print("ids: ", ids)
        print("sum: ", sum)

if __name__ == "__main__":
    main()