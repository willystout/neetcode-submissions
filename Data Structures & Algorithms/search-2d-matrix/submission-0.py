class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        L, R = 0, len(matrix) - 1

        while L <= R:
            mid1 = (L + R) // 2
            if target < matrix[mid1][0]:
                R = mid1 - 1
            elif target > matrix[mid1][len(matrix[mid1]) - 1]:
                L = mid1 + 1
            else:
                break
        l = 0
        r = len(matrix[mid1]) - 1
        while l <= r:
            midp = (l + r) // 2
            if target < matrix[mid1][midp]:
                r = midp - 1
            elif target > matrix[mid1][midp]:
                l = midp + 1
            else:
                return True
        return False