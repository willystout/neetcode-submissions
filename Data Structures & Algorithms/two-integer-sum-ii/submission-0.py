class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = 0, len(numbers) - 1
        while i < j:
            theSum = numbers[i] + numbers[j]
            if target < theSum:
                j -= 1
            elif target > theSum:
                i += 1
            else:
                return [i + 1, j + 1]
        return []
        