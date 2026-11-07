class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        max_count = -float("inf")
        curr = 0
        for i in range(0, n):
            if curr <= 0:
                curr = 0

            num = nums[i]
            curr += num

            max_count = max(curr, max_count, nums[i])
        return max_count
            