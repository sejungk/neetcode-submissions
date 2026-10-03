class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(openings, closings, string):
            if openings < 0 or closings < 0:
                return 

            if openings == 0 and closings == 0:
                res.append(string)
                return 
            
            dfs(openings - 1, closings, string + "(")
            if openings < closings:
                dfs(openings, closings - 1, string + ")")

        dfs(n, n, "")
        return res
