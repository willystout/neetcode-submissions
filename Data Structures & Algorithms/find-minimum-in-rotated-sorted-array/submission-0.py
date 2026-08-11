class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        # if nums[r] < nums[l] go right from mid

        while l <= r:
            mid = (l + r) // 2
            print(nums[l], nums[mid], nums[r])
            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[l] < nums[mid]:
                r = mid - 1
            elif nums[mid] < nums[l]:
                r = mid
                l += 1
            else:
                break
            
        return nums[mid]