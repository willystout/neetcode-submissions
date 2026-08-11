class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "EMPTYLIST"
        return "&&%12%^32123**&&^^&##$!@#!@!!!".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "EMPTYLIST": return []
        return s.split("&&%12%^32123**&&^^&##$!@#!@!!!")
