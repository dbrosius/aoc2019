FILENAME = "input2.txt"


def main1(noun, verb):
    with open(FILENAME) as f:
        line = f.readline()
    thelist = line.split(",")
    thelist = [int(it) for it in thelist]
    thelist[1] = noun
    thelist[2] = verb
    iterator = iter(thelist)
    opcode = next(iterator)
    while opcode != 99:
        op1 = next(iterator)
        op2 = next(iterator)
        loc = next(iterator)
        if opcode == 1:
            res = thelist[op1] + thelist[op2]
        elif opcode == 2:
            res = thelist[op1] * thelist[op2]
        else:
            print("Danger, Will Robinson!")
            return
        thelist[loc] = res
        opcode = next(iterator)
    return thelist[0]


def main2():
    for noun in range(0, 100):
        for verb in range(0, 100):
            output = main1(noun, verb)
            if output == 19690720:
                return noun, verb


if __name__ == "__main__":
    print(main1(12, 2))
    print(main2())