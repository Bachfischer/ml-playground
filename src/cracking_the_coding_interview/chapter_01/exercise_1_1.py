"""
The time complexity for this code is O(n), where n is the length of the string.
The space complexity is O(1).
"""


def is_ascii(string_to_check: str):
    return all(ord(char) < 128 for char in string_to_check)


def is_unique(string_to_check: str) -> bool:
    alphabet = {}

    print("Test string is: " + string_to_check)
    if is_ascii(string_to_check):

        for char in string_to_check:
            if ord(char) in alphabet:
                print("Input string does not have unique characters!")
                return False
            else:
                alphabet[ord(char)] = 1

        # After all characters in string have been checked
        print("Input string has only unique characters")
        return True
    else:
        raise ValueError("Input string is not ASCII")


def main():
    test_string = "asdbasdasc"
    test_string_2 = "asd"
    test_string_3 = "ßßß%a"

    try:
        is_unique(test_string)
        is_unique(test_string_2)
        is_unique(test_string_3)
    except ValueError:
        print("Input string is not ASCII")


if __name__ == "__main__":
    # execute only if run as a script
    main()
