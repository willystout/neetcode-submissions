class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            if str(count) in res:
                res[str(count)].append(s)
            else:
                res[str(count)] = [s]
        
        return list(res.values())

            