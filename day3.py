import numpy as np

FILENAME = "input3.txt"


def follow_direction(grid, location, direction):
    heading = direction[0]
    amount = int(direction[1:])
    if heading == "U":
        pass
    elif heading == "R":
        pass
    elif heading == "D":
        pass
    elif heading == "L":
        pass
    else:
        print("Danger, Will Robinson!")
        return


def main1():
    with open(FILENAME) as f:
        line1 = f.readline()
        line2 = f.readline()
    dirlist1 = line1.split(",")
    dirlist2 = line2.split(",")
    grid = np.zeros((501, 501))
    start1 = (250, 250)
    start2 = (250, 250)
    for direction in dirlist1:
        pass


if __name__ == "__main__":
    main1()
