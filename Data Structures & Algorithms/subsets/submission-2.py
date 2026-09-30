# class Solution:
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     res = [[]]
        
    #     for num in nums:
    #         n = len(res)
    #             for j in range(n):
    #                 new_item = res[i] + [nums[i]]
    #                 res.append(new_item)

    #     dfs()
    #     return res

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for num in nums:
            new_subsets = []

            for subset in res:
                subset = subset.copy()
                subset.append(num)
                new_subsets.append(subset)
            res.extend(new_subsets)
            
        return res