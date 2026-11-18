class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        clist = sorted(count, key=count.get, reverse=True)
        # print(clist[:k])
        return clist[:k]