class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        # print(nums)
        maxCount = 1
        localCount = 1
        for i in range(len(nums) - 1):
            # print(nums[i], " vs ", nums[i + 1])
            if nums[i] + 1 == nums[i + 1]:
                # print("Is a sequence. ")
                localCount += 1
            elif nums[i] == nums[i + 1]:
                continue
            else:
                # print("Is not a sequence")
                localCount = 1
            maxCount = max(maxCount, localCount)
            # print("new maxCount: ", maxCount)
        return maxCount