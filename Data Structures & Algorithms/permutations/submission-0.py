class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def combinations(nums, arr):
            if len(nums) == 0:
                res.append(arr.copy())
                return 
            
            for i in range(len(nums)):
                num = nums.pop(i)
                combinations(nums, arr + [num])
                nums.insert(i, num)

        combinations(nums, [])
        return res