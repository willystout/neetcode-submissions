class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i in range(len(nums)):
            target_num = target - nums[i]
            if target_num in num_map:
                return [num_map[target_num], i]
            num_map[nums[i]] = i
