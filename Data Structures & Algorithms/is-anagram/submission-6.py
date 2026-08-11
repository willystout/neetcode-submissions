class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        for i in s:
            if i not in s_map:
                s_map[i] = 0
            else:
                s_map[i] += 1
        for j in t:
            print(j)
            if j not in t_map:
                t_map[j] = 0
            else:
                t_map[j] += 1
        if s_map != t_map:
            return False
        return True
        