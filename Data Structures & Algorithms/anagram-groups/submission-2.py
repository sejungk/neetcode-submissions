class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = {}

        for str in strs:
            key = "".join(sorted(str))
            if key in keys:
                keys[key].append(str)
            else:
                keys[key] = [str]
        
        return list(keys.values())
