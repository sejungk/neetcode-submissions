class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        max_start = max(start for start, end in intervals)

        # At each start coordinate, store the farthest interval end + 1.
        max_interval_ends = [0] * (max_start + 1)

        for start, end in intervals:
            max_interval_ends[start] = max(
                end + 1,
                max_interval_ends[start]
            )

        res = []
        curr_start = -1
        curr_end = -1

        for i in range(len(max_interval_ends)):
            end_marker = max_interval_ends[i]

            if end_marker != 0:
                # if this is the beginning
                if curr_start == -1:
                    curr_start = i
                curr_end = max(curr_end, end_marker - 1)

            if i == curr_end:
                res.append([curr_start, curr_end])

                # reset vars
                curr_start = -1
                curr_end = -1

        if curr_start != -1:
            res.append([curr_start, curr_end])

        return res