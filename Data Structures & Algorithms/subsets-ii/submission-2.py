class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        def backtrack(i, arr):
            if i == n:
                res.append(arr.copy())
                return
            
            arr.append(nums[i])
            backtrack(i + 1, arr)
            arr.pop()
            
            while (i + 1) < n and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, arr)

        backtrack(0, [])
        return res