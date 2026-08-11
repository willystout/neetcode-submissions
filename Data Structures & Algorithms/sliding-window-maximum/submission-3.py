class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i, j = 0, k
        max_list = [0]*(len(nums) - k + 1)
        for x in range(len(nums)):
            if j > len(nums):
                break
            max_list[x] = max(nums[i:j])
            i += 1
            j += 1

        return max_list


