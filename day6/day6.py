def menu():
    print("Day 6")

def read_input():
    try:
        with open(f'day6.txt', 'r') as f:
            data = f.read().splitlines()
        return data
    except FileNotFoundError:
        print(f"File not found")
        return None
    except Exception as e:
        print(f"Problem with reading file: {e}")
        return None

def beatRecord(pair):
    ways = []

    for time, distance in pair:
        way = 0

        for holdTime in range(time):
            speed = holdTime
            raceTime = time - holdTime
            distanceTraveled = speed * raceTime

            if distanceTraveled > distance:
                way += 1

        ways.append(way)

    return ways

def makePair(data):
    time = [int(x) for x in data[0].split(': ')[1].split(' ') if x != '']
    distance = [int(x) for x in data[1].split(': ')[1].split(' ') if x != '']

    pair = [(time[i], distance[i]) for i in range(len(time))]

    return pair

def main():
    data = read_input()

    if data is not None:
        pair = makePair(data)
        beatRecordWays = beatRecord(pair)

        result = 1
        for ways in beatRecordWays:
            result *= ways

        print("Result:", result)

if __name__ == "__main__":
    main()
