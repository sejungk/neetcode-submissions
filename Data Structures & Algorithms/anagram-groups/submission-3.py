class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}

        for str in strs:
            count = [0] * 26
            for char in str:
                count[ord(char) - ord('a')] += 1
            key = tuple(count)
        
            keys.setdefault(key, []).append(str)
        return list(keys.values())
