class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = {}
        for num in nums:
            result[num] = result.get(num, 0) + 1
        sorted_list = sorted(result.items(), key=lambda p: -p[1])
        keys = [k for k, _ in sorted_list]
        return keys[:k]