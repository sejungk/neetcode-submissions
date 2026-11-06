class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_count = 0
        for num in nums:
            if (num - 1) in nums_set:
                continue
            
            count = 0
            curr = num
            while curr in nums_set:
                count += 1
                curr = curr + 1
            
            max_count = max(count, max_count)

        return max_count