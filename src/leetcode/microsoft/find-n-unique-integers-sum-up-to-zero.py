# Source: https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/submissions/

# Time complexity: O(N)
# Space complexity: O(N)

class Solution:
    def sumZero(self, n: int) -> List[int]:

        result = set()

        if n % 2 == 1:
            result.add(0)
            n = n - 1

        number_of_random_integers = n / 2
        counter = 1

        while number_of_random_integers > 0:
            result.add(counter)
            result.add(-counter)

            counter += 1
            number_of_random_integers = number_of_random_integers - 1

        return list(result)
