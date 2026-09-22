class Solution:
    def maxArea(self, heights: List[int]) -> int:
        i, j = 0, len(heights) - 1
        heightMax = 0
        while i < j:
            if heights[i] > heights[j]:
                a = heights[j]
            elif heights[i] < heights[j]:
                a = heights[i]
            else:
                a = heights[j]
            currMax = (j - i) * a
            heightMax = max(heightMax, currMax)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return heightMax
