# Source: https://leetcode.com/discuss/interview-question/406031/

# Time Complexity: O(N)
# Space Complexity: O(1)
def find_largest_k(array: list) -> int:
    array.sort(reverse = True)

    for element in array:
        if element <= 0:
            return 0
        elif -element in array:
            return element

print(find_largest_k([3, 2, -2, 5, -3]))
# response: 3