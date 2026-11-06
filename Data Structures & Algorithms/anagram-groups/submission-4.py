class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        keys = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))

            keys[key].append(s)

        res = []
        for lists in keys.values():
            res.append(lists)

        return res