class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        print(s)
        if len(s) == 1:
            return [""]
        decoded = []
        i = 0
        while i < len(s):
            j = 0
            countstr = ""
            while s[i] != '#':
                countstr += s[i]
                i += 1
            count = int(countstr)
            newstr = ""
            i += 1
            while j < count:
                newstr += str(s[i])
                j += 1
                i += 1
            print("new str: ", newstr)
            decoded.append(newstr)

        return decoded
