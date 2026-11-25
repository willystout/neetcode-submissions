class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res


    def decode(self, s: str) -> List[str]:
        numToString = ""
        num = 0
        string = ""
        res = []
        i = 0
        while i < len(s) - 1:
            # print("s of i is: ", s[i])
            while s[i] != '#':
                # print("adding: ", s[i])
                numToString += s[i]
                i += 1
            # print("num to string is: ", numToString)
            num = int(numToString) + i
            i += 1
            while i < len(s) and i <= num:
                string += s[i]
                i += 1
            res.append(string)
            # print("res is ", res)
            string = ""
            numToString = ""
            # print("-")

        return res
