FILENAME = "input1.txt"


def main1():
    total_fuel = 0
    with open(FILENAME) as f:
        for line in f:
            total_fuel += int(line) // 3 - 2
    print(total_fuel)


def recurse_fuel(mass):
    total_fuel = 0
    fuel = mass // 3 - 2
    while fuel > 0:
        total_fuel += fuel
        fuel = fuel // 3 - 2
    return total_fuel


def main2():
    total_fuel = 0
    with open(FILENAME) as f:
        for line in f:
            total_fuel += recurse_fuel(int(line))
    print(total_fuel)


if __name__ == "__main__":
    main1()
    main2()