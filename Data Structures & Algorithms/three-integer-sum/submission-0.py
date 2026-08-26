# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         distinct_nums = set(nums)
#         pairs = defaultdict(list)        
#         n = len(nums)

#         for i in range(n):
#             for j in range(i + 1, n):
#                 num1 = nums[i]
#                 num2 = nums[j]
#                 sum = num1 + num2

#                 pairs[sum].append([i, j])
        
#         result = []
#         for key, value in pairs:
#             diff = 0 - key
#             if diff in distinct_nums:
#                 for pair in value:
                    

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        n = len(nums)

        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    num1 = nums[i]
                    num2 = nums[j]
                    num3 = nums[k]
                    sum = num1 + num2 + num3
                    
                    if sum == 0:
                        result.add(tuple(sorted([num1, num2, num3])))
        
        return list(result)
                    