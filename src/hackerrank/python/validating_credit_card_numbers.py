# Link to Question: https://www.hackerrank.com/challenges/validating-credit-card-number/

# Enter your code here. Read input from STDIN. Print output to STDOUT

def check_start_digit(creditcard_number):
    if creditcard_number[0] != '4' and creditcard_number[0] != '5' and \
            creditcard_number[0] != '6':
        print("Invalid")
        return False
    return True


def extract_digits_and_check_separator(creditcard_number):
    creditcard_numbers = []

    group_counter = 0
    for number in creditcard_number:
        if number.isdigit():
            group_counter += 1
            creditcard_numbers.append(number)
        elif number == "-":
            if group_counter != 4:
                print("Invalid")
                return False
            else:
                group_counter = 0
                continue
        else:
            print("Invalid")
            return False
    return creditcard_numbers


def check_length(creditcard_number):
    if len(creditcard_number) != 16:
        print("Invalid")
        return False

    return True


def check_consecutive_repeated_digits(creditcard_number):
    consecutive_element_counter = 0
    last_number = creditcard_number[0]

    for number in creditcard_number:
        if number == last_number:
            consecutive_element_counter += 1
            if consecutive_element_counter >= 4:
                print("Invalid")
                return False
        else:
            consecutive_element_counter = 1
            last_number = number

    return True


# read in the number of credit cards
number_of_cards = int(input())

# assert(number_of_cards > 0 and number_of_cards < 100, "Invalid number of credit cards specified")

for card in range(number_of_cards):
    creditcard_number = input()
    creditcard_number = creditcard_number.rstrip()

    # Condition 1
    if check_start_digit(creditcard_number) is not True:
        continue

    # Condition 3, 4 and 5
    creditcard_number_list = extract_digits_and_check_separator(
        creditcard_number)

    if isinstance(creditcard_number_list, list) is not True:
        continue

    # Condition 2
    if check_length(creditcard_number_list) is not True:
        continue

    # Condition 6
    if check_consecutive_repeated_digits(creditcard_number_list) is not True:
        continue

    print("Valid")

