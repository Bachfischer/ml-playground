# Source: https://leetcode.com/discuss/interview-question/988051/Microsoft-or-OA
import unittest

class TestFindMaxPossibleValue(unittest.TestCase):

    def test_numbers(self):
        self.assertEqual(find_maximum_possible_value_by_inserting_five(1234), 51234)
        self.assertEqual(find_maximum_possible_value_by_inserting_five(7643), 76543)
        self.assertEqual(find_maximum_possible_value_by_inserting_five(0), 50)
        self.assertEqual(find_maximum_possible_value_by_inserting_five(1234), 51234)
        self.assertEqual(find_maximum_possible_value_by_inserting_five(-661), -5661)


def find_maximum_possible_value_by_inserting_five(given_value: int) -> int:

    # convert int to string
    given_value = str(given_value)

    if given_value[0] != '-':
        given_value = '+' + given_value

    max_value = None

    # for each possible position
    for i in range(1, len(given_value)):
        candidate_number = given_value[:i] + '5' + given_value[i:]

        if max_value is None or int(candidate_number) > max_value:
            max_value = int(candidate_number)

    return max_value


if __name__ == "__main__":
    print(find_maximum_possible_value_by_inserting_five(-661))