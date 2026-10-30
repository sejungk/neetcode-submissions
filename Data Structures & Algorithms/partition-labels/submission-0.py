class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_idx = {}
        for idx, char in enumerate(s):
            last_idx[char] = idx
        
        res = []
        size = 0
        end = 0

        for idx, char in enumerate(s):
            size += 1
            end = max(end, last_idx[char])

            if idx == end:
                res.append(size)
                size = 0
        return res