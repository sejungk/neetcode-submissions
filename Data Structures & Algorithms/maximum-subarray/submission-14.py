class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_count = nums[0]
        curr = 0
        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            max_count = max(max_count, curr)
        return max_count

            