# Source: Maximum Length of a Concatenated String with Unique Characters

# Time Complexity: O(2^N) (since for each element of the input array, the unique array potentially doubles in size during inner loop)
# Space Complexity: O(2^N)

class Solution:
    def maxLength(self, arr: list[str]) -> int:
        maxlen = 0
        unique = ['']

        def is_unique(s):
            return len(s) == len(set(s))

        for word in arr:
            for j in unique:
                tmp = word + j
                if is_unique(tmp):
                    unique.append(tmp)
                    maxlen = max(maxlen, len(tmp))

        return maxlen