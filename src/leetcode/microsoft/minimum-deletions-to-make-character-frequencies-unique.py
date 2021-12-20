# Source: https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/submissions/

# Time complexity: O(N) where N is number of characters
# Space compexity: O(1) as we store 26 frequencies as maximum

class Solution:
    def minDeletions(self, s: str) -> int:

        import collections

        # get frequencies for characters a-z
        frequencies = collections.Counter(s)

        # order by frequencies
        frequency_values = list(frequencies.values())
        frequency_values.sort(reverse=True)

        # find minimum number of modifications

        number_of_modifications = 0
        has_appeared_before = set()

        for frequency in frequency_values:
            if frequency not in has_appeared_before:
                has_appeared_before.add(frequency)

            else:
                while frequency in has_appeared_before and frequency > 0:
                    number_of_modifications += 1
                    frequency = frequency - 1

                has_appeared_before.add(frequency)

        return number_of_modifications
