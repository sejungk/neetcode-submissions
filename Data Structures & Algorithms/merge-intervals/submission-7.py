class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_end = max(end for start, end in intervals)

        mp = [-1] * (max_end + 1)
        for start, end in intervals:
            mp[start] = max(mp[start], end)
        
        res = []
        start = -1
        end = -1
        for i in range(0, max_end + 1):
            if mp[i] != -1:
                if end == -1:
                    start = i
                    end = mp[i]
                else:
                    end = max(end, mp[i])

            if i == end:
                res.append([start, end])
                end = -1
                start = -1

        return res

            