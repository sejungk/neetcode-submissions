class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        seen = defaultdict(int)
        max_val = {}
        res = []

        l = 0
        for r in range(len(nums)):
            seen[nums[r]] += 1

            if r - l + 1 == k:
                max_val = -float("inf")
                for key in seen:
                    max_val = max(key, max_val)

                seen[nums[l]] -= 1
                if seen[nums[l]] == 0:
                    del seen[nums[l]]
                l += 1  

                res.append(max_val)
        return res