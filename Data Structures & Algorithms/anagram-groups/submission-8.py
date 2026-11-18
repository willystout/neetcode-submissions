class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)
            if key not in resMap:
                resMap[key] = [s]
            else:
                resMap[key].append(s)
        return list(resMap.values())
            



