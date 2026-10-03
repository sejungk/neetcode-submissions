class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def is_palindrome(string):
            return string == string[::-1]

        def create_palindromes(substrings, i):
            if i == len(s):
                if substrings[-1] and is_palindrome(substrings[-1]): 
                    res.append(substrings.copy())
                return

            substrings[-1] += s[i]
            if is_palindrome(substrings[-1]):
                substrings.append("")
                create_palindromes(substrings, i + 1)
                substrings.pop()
                
            create_palindromes(substrings, i + 1)

        create_palindromes([""], 0)
        return res
