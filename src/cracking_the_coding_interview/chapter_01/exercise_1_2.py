"""
Check Permutation: 
Given two strings,write a method to decide if one is a permutation of the other.
"""


def check_permutation(string_to_compare_1: str, string_to_compare_2: str) -> bool:
    string_to_compare_1 = sorted(string_to_compare_1)
    string_to_compare_2 = sorted(string_to_compare_2)

    if string_to_compare_1 == string_to_compare_2:
        return True
    else:
        return False


"""
***Solution below is for different type of exercise***


def check_permutation(string_to_compare_1: str, string_to_compare_2: str) -> bool:
    position_start = 0
    position_end = 0
    matching_mode = False
    for index in range(0, len(string_to_compare_2)):
        if not matching_mode and string_to_compare_2[index] == string_to_compare_1[0]:
            matching_mode = True
            position_start = index
            position_end = index
        elif matching_mode and string_to_compare_2[index] == string_to_compare_1[index-position_start]:
            position_end = index
        else:
            matching_mode = False

        if position_end - position_start +1 == len(string_to_compare_1):
            return True

    return False
"""


def main():
    string_to_compare_1 = "dog_"
    string_to_compare_2 = "god"

    is_permutation = check_permutation(string_to_compare_1, string_to_compare_2)
    if is_permutation:
        print("String: " + string_to_compare_1 + " is a permutation of " + string_to_compare_2)
    else:
        print("String: " + string_to_compare_1 + " is not a permutation of " + string_to_compare_2)


if __name__ == "__main__":
    main()
