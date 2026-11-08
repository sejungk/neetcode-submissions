class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]

        curr_max = 1
        curr_min = 1
        for i in range(n):
            temp = curr_max
            curr_max = max(curr_max * nums[i], curr_min * nums[i], nums[i])
            curr_min = min (temp * nums[i], curr_min * nums[i], nums[i])
            
            res = max(res, curr_max)

            if nums[i] == 0:
                curr_max = 1
                curr_min = 1

        return res