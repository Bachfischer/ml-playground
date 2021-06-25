def urlify(string_to_convert: str, string_length: int) -> str:
    converted_string = ""
    counter = 0
    for char in string_to_convert:
        if counter == string_length:
            return converted_string
        elif char.isspace():
            converted_string += "%20"
        else:
            converted_string += char

        counter += 1

    return converted_string


def main():
    input_string = "Mr John Smith   "
    converted_string = urlify(input_string, len(input_string.strip()))
    print(converted_string)


if __name__ == "__main__":
    main()