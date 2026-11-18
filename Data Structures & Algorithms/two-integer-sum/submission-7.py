class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        resMap = {}
        for i in range(len(nums)):
            # print("current number: ", nums[i])
            targetNum = target - nums[i]
            # print("targetNum: ", targetNum)
            if targetNum in resMap:
                return [resMap[targetNum], i]
            # print("target number not in hashmap: ")
            resMap[nums[i]] = i
            
