# Source: https://leetcode.com/discuss/interview-question/364618/
# Time Complexity: O(N logN)
# Space Complexity: O(1)

def make_piles_equal_height(piles: list) -> int:

    number_of_operations = 0

    #sort list of piles in descending order
    piles.sort(reverse=True)

    max_element = piles[0]
    i = 1
    while i <= len(piles) -1:

        if max_element != piles[i]:
            piles[i-1] = piles[i]
            number_of_operations += 1
            i = 1
            max_element = piles[0]
        elif i == len(piles) - 1:
            return number_of_operations
        else:
            i += 1

def solution(piles: list) -> int:
    total = 0
    l = sorted(piles, reverse=True)
    for i in range(0, len(l) - 1):
        if l[i] > l[i + 1]:
            # need to change up to i piles
            total += i + 1
    return total

piles = [5,2,1]
print(make_piles_equal_height(piles))

piles = [5,2,1]
print(solution(piles))