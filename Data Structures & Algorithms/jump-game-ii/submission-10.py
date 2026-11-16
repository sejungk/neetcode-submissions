class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = 0
        res = 0

        while r < n - 1:
            farthest = r

            for j in range(l, r + 1):
                farthest = max(farthest, j +  nums[j])

            l = r + 1
            r = farthest
            res += 1
            
        return res
            
