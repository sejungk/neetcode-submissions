class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curr_min = 1
        curr_max = 1

        for num in nums:
            val = curr_max * num
            curr_max = max(num * curr_max, num * curr_min, num)
            curr_min = min(val, num * curr_min, num)
            res = max(res, curr_max)
        return res