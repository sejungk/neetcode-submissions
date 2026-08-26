class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for string in strs:
            key = ''.join(sorted(string))

            if key not in dict:
                dict[key] = []

            dict[key].append(string)

        result = []
        for key in dict:
            result.append(dict[key])
        
        return result
            