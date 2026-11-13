class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(opens, closes, parens):
            if opens == 0 and closes == 0:
                res.append("".join(parens))
                return

            if opens > 0:
                parens.append("(")
                dfs(opens - 1, closes, parens)
                parens.pop()
            
            if opens < closes:
                parens.append(")")
                dfs(opens, closes - 1, parens)
                parens.pop()

        dfs(n, n, [])
        return res