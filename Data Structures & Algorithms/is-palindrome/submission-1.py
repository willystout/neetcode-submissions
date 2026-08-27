import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean_text = re.sub(r'[^A-Za-z0-9]+', '', s)
        i, j = 0, len(clean_text) - 1
        while i < j and j >= 0:
            if clean_text[i] != clean_text[j]:
                print("i: ", clean_text[i])
                print("j: ", clean_text[j])
                return False
            i += 1
            j -= 1
        return True