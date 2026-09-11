class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        max_len = 1
        curr = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                curr += 1
            elif nums[i] > nums[i - 1] + 1:
                curr = 1
            max_len = max(max_len, curr)
        return max_len
