class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        seen = set(nums)

        for i in nums:
            if i - 1 not in seen:
                j = i
                while j in seen:
                    j += 1
                max_length = max(max_length, j - i)
            
        return max_length