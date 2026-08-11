class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        maxCount = 0
        countSet = set(nums)
        for n in nums:
            if n - 1 not in countSet:
                length = 0
                while n + length in countSet:
                    length += 1
                maxCount = max(length, maxCount)
        return maxCount