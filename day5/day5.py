def menu():
    print("Day 5")

def read_input():
    try:
        with open(f'day5.txt', 'r') as f:
            data = f.read().splitlines()
        return data
    except FileNotFoundError:
        print(f"File not found")
        return None
    except Exception as e:
        print(f"Problem with reading file: {e}")
        return None

def mapsValue(data):
    maps = []
    map = []

    for line in data[1:]:
        if line == '':
            if map:
                maps.append(map)
                map = []
        else:
            map.append(line)
    if map:
        maps.append(map)

    return maps

def seedValue(source, maps):
    for m in maps:
        values = m[1:]

        for i in values:
            i = [int(x) for x in i.split(' ')]
            check = range(i[1], i[1] + i[2])

            if source in check:
                distance = source - i[1]
                source = i[0] + distance
                break

    return source

def main():
    data = read_input()

    if data is not None:
        seeds = [int(x) for x in data[0].split(': ')[1].split(' ')]
        maps = mapsValue(data)

        if maps is not None:
            value = [seedValue(seed, maps) for seed in seeds]
            print("value:", min(value))

if __name__ == "__main__":
    main()
