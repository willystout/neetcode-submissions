from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        uniquenums = list(set(nums))
        nums = sorted(uniquenums)
        res = defaultdict()
        for num in nums:
            if (num - 1) in res:
                res[num - 1] += 1
                res[num] = res[num - 1]
            if (num - 1) not in res:
                res[num] = 1
        return max(res.values())
        