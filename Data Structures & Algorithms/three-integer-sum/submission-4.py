class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        output = []
        for i in range(n):
            left = i + 1
            right = n - 1
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    while left < n - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                elif sum < 0:
                    while left < n - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                else:
                    while right > i and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                
        return output