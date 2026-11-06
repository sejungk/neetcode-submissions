class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sums = [1] * n

        prev = nums[0]
        for i in range(1, n):
            sums[i] = prev
            prev *= nums[i]
        
        prev = 1
        for i in range(n - 1, -1, -1):
            sums[i] *= prev
            prev *= nums[i]

        res = []
        for i in range(n):
            res.append(sums[i])

        return res