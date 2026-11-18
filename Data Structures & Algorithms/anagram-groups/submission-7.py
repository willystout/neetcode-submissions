class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            if tuple(count) not in resMap:
                resMap[tuple(count)] = [s]
            else:
                resMap[tuple(count)].append(s)
        return list(resMap.values())
            



