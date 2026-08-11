class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_list = {}
        for num in nums:
            if num in nums_list:
                return True
            else:
                nums_list[num] = 0
        return False
        