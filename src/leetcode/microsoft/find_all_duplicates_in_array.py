# Source: https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        list_of_duplicates = []

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                # found duplicates
                list_of_duplicates.append(nums[i])

        return list_of_duplicates

solution = Solution()

nums = [4,3,2,7,8,2,3,1]
print(solution.findDuplicates(nums))