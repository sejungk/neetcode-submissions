class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        rob1 = 0
        rob2 = 0

        for num in nums:
            curr = max(num + rob2, rob1)
            rob2 = rob1
            rob1 = curr

        return rob1