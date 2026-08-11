class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        j = 1
        if(len(nums) < 1):
            return False
        
        while(i < len(nums)):
            j = i + 1
            while(j < len(nums)):
                if(nums[i] == nums[j]):
                    return True
                j += 1
            i += 1
        return False
         