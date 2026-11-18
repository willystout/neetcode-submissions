class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        resMap = {}
        for s in strs:
            newMap = {}
            for c in s:
                newMap[c] = 1 + newMap.get(c, 0)
            key = str(sorted(newMap.items()))
            if key not in resMap:
                resMap[key] = []
                resMap[key].append(s)
            else:
                resMap[key].append(s)
        return list(resMap.values())
            



