class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        n = len(s)
        
        res = []
        i = 0
        while i < n:
            j = i
            while j < n and s[j] != "#":
                j += 1
            
            s_len = int(s[i:j])

            word = []
            for k in range(j + 1, j + s_len + 1):
                word.append(s[k])
            
            res.append("".join(word))
            i = j + s_len + 1
        return res


