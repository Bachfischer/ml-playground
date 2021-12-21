# Source: https://leetcode.com/discuss/interview-question/558015/Microsoft-OA

# Time Complexity: O(N log N) (for sorting the array)
# Space complexity: O(1)

import unittest

class TestCases(unittest.TestCase):

    def test_check_if_elements_differ_by_one(self):
        self.assertFalse(check_if_elements_differ_by_one([7]))
        self.assertTrue(check_if_elements_differ_by_one([4,3]))
        self.assertTrue(check_if_elements_differ_by_one([11, 1, 8, 12, 14]))
        self.assertFalse(check_if_elements_differ_by_one([5, 5, 5, 5, 5]))
        self.assertTrue(check_if_elements_differ_by_one([4, 10, 8, 5, 9]))


def check_if_elements_differ_by_one(array : list[int]) -> bool:
    # sort in ascending order
    array.sort()

    # check if elements differ by one
    for i in range(1, len(array)):
        if array[i] - array[i-1] == 1:
            return True

    return False



if __name__ == "__main__":
    unittest.main()