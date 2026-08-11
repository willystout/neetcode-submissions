class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        L, R = 0, len(s) - 1
        while L < R:
            if s[L] != s[R]:
                print(L, R, s[L], s[R])
                return False
            else:
                L += 1
                R -= 1
        return True