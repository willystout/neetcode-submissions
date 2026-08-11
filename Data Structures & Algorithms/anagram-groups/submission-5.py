class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for s in strs:
            key = "".join(sorted(s))
            if key not in result:
                result[key] = [s]
            else:
                result[key].append(s)
        return list(result.values())