class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(arr):
            rob2 = rob1 = 0

            for num in arr:
                curr = max(rob2 + num, rob1)
                rob2 = rob1
                rob1 = curr

            return rob1

        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))

    