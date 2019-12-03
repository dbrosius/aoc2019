FILENAME = "input2.txt"


def main1():
    with open(FILENAME) as f:
        line = f.readline()
        thelist = line.split(",")
    thelist[1] = "12"
    thelist[2] = "2"
    iterator = iter(thelist)
    opcode = int(next(iterator))
    while opcode != 99:
        op1 = int(next(iterator))
        op2 = int(next(iterator))
        loc = int(next(iterator))
        if opcode == 1:
            res = int(thelist[op1]) + int(thelist[op2])
        elif opcode == 2:
            res = int(thelist[op1]) * int(thelist[op2])
        else:
            print("Danger, Will Robinson!")
            return
        thelist[loc] = res
        opcode = int(next(iterator))
    print(thelist[0])


if __name__ == "__main__":
    main1()