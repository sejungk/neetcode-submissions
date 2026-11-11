class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = [[]]

        for num in nums:
            res += [subset + [num] for subset in res]

        return res
#    ij
# [1,2,3]
# [1], [2], [3]
