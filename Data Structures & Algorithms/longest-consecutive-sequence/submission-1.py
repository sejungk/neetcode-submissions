class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        longest = 1
        n = len(nums)

        if n == 0:
            return 0

        currConsecutive = 1
        for i in range(1, n):
            prev = i - 1
            
            if nums[i] - nums[prev] == 1:
                currConsecutive += 1
            elif nums[i] == nums[prev]:
                continue
            else:
                longest = max(longest, currConsecutive)
                currConsecutive = 1
        longest = max(longest, currConsecutive)
        return longest
