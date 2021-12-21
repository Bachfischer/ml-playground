# Source: https://leetcode.com/problems/fizz-buzz/
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = {}

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                answer[i] = "FizzBuzz"
            elif i % 3 == 0:
                answer[i] = "Fizz"
            elif i % 5 == 0:
                answer[i] = "Buzz"
            else:
                answer[i] = str(i)

        return list(answer.values())