class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def is_pali(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        res = []
        def dfs(i, arr):
            if i == len(s):
                res.append(arr.copy())
                return
            
            for j in range(i, len(s)):
                if is_pali(i, j):
                    arr.append(s[i:j + 1])
                    dfs(j + 1, arr)
                    arr.pop()

        dfs(0, [])
        return res