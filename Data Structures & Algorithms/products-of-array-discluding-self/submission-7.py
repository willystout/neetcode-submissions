class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n
        i = 1
        while i < n:
            left[i] = nums[i-1] * left[i-1]
            i += 1
        j = n - 2
        while j >= 0:
            right[j] = nums[j+1] * right[j+1]
            j -= 1
        return [x * y for x, y in zip(left, right)]