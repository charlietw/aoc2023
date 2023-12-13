FILENAME = "input.txt"


def open_file():
    return f


def get_digit(character):
    try:
        return int(character)
    except ValueError:
        return None


def get_all_digits(word):
    digits = []
    for c in word:
        if get_digit(c) is not None:
            digits.append(get_digit(c))
    return digits


def get_number_of_digits(digits_array):
    return len(digits_array)


def get_first_digit(word):
    return get_all_digits(word)[0]


def get_last_digit(word):
    digits = get_all_digits(word)
    number_of_digits = get_number_of_digits(digits)
    index = number_of_digits - 1
    return get_all_digits(word)[index]


def add_first_and_last_digit(word):
    first_digit = get_first_digit(word)
    last_digit = get_last_digit(word)
    combined_string = str(first_digit) + str(last_digit)
    print(f"Word is: {word}, output is {combined_string}")
    return int(combined_string)


def main():
    result = 0
    with open(FILENAME) as file:
        for f in file:
            word_result = add_first_and_last_digit(f)
            result = result + word_result
            print(result)
    return result


if __name__ == "__main__":
    main()
