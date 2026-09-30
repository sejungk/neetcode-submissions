class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            for j in range(len(res)):
                new_item = res[j] + [num]
                res.append(new_item)
        return res

# class Solution:
#     def subsets(self, nums: List[int]) -> List[List[int]]:
#         res = [[]]
        
#         for num in nums:
#             new_subsets = []

#             for subset in res:
#                 subset = subset.copy()
#                 subset.append(num)
#                 new_subsets.append(subset)
#             res += new_subsets
            
#         return res