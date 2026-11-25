class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}
        for i in range(len(nums)):
            tar = target - nums[i]
            if tar in res:
                return [res[tar], i]
            res[nums[i]] = i

        