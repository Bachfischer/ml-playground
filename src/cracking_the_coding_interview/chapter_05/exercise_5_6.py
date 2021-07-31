"""
Conversion:
Write a function to determine the number of bits you would need to flip to convert integer A to integer B.
"""

def find_number_of_bits_to_flip(number_1, number_2):
    count = 0

    # since, the numbers are less than 2^31
    # run the loop from '0' to '31' only
    for i in range(0, 32):

        # right shift both the numbers by 'i' and
        # check if the bit at the 0th position is different
        if (((number_1 >> i) & 1) != ((number_2 >> i) & 1)):
            count = count + 1

    print("Number of different bits :", count)

number_1 = 29
number_2 = 15

find_number_of_bits_to_flip(number_1, number_2)