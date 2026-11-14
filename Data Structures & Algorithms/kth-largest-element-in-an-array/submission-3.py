class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        l = 0
        r = n - 1
        target = n - k
        while l <= r:
            partition = r
            p = l
            for i in range(l, r):
                if nums[i] < nums[partition]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            
            nums[partition], nums[p] = nums[p], nums[partition]
            if p == target:
                return nums[p]
            elif p > target:
                r = p - 1
            else:
                l = p + 1