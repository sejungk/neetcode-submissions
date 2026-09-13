class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        res = float("inf")

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                res = min(res, nums[mid])
                right = mid - 1
        
        return res
           

