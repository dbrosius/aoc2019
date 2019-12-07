INPUT1 = 197487
INPUT2 = 673251


def check_value1(value):
    has_repeat = False
    ascending = True
    last_number = "0"
    str_value = str(value)
    for the_char in str_value:
        if the_char == last_number:
            has_repeat = True
        if the_char < last_number:
            ascending = False
        last_number = the_char
    return has_repeat and ascending


def check_value2(value):
    has_repeat = False
    ascending = True
    last_last_number = "."
    last_number = "/"
    str_value = str(value)
    for the_char in str_value:
        if the_char == last_number:
            has_repeat = True
        if the_char < last_number:
            ascending = False
        last_last_number = last_number
        last_number = the_char
    return has_repeat and ascending


def main(check_value):
    valid = []
    invalid = []
    for value in range(INPUT1, INPUT2 + 1):
        if check_value(value):
            valid.append(value)
        else:
            invalid.append(value)
    return len(valid)


if __name__ == "__main__":
    print(main(check_value1))
    print(main(check_value2))
