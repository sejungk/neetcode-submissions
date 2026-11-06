class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        pre = [1] * n
        post = [1] * n

        for i in range(1, n):
            pre[i] = nums[i - 1] * pre[i - 1]
        
        for i in range(n - 2, -1, -1):
            post[i] = nums[i + 1] * post[i + 1]
        
        for i in range(n):
            res[i] = pre[i] * post[i]

        return res