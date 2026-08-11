class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        char_count1 = defaultdict(int)
        char_count2 = defaultdict(int)
        for i in range(len(s)):
            char_count1[s[i]] += 1
            char_count2[t[i]] += 1
        return char_count1 == char_count2
        
        