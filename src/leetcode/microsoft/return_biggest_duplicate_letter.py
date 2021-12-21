# Source: https://leetcode.com/discuss/interview-question/988051/Microsoft-or-OA
# Time Complexity: O(N) since we may need to traverse the whole array
# Space Compexity: O(1)


def return_biggest_duplicate_letter(input: str) -> str:
    sorted_letters = sorted(input)
    response = 'NO'

    for i in range(0, len(input)):
        current_letter = sorted_letters[i]

        if not current_letter.isupper():
            break
        elif current_letter.lower() in sorted_letters:
            response = current_letter

    return response


input = "aaacbAbCd"
print(return_biggest_duplicate_letter(input))