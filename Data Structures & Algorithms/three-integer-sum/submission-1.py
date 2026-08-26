class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i - 1] == nums[i]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                num1 = nums[i]
                num2 = nums[left]
                num3 = nums[right]
                sum = num1 + num2 + num3

                if sum == 0:
                    result.append([num1, num2, num3])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif sum < 0:
                    left += 1
                else:
                    right -= 1
        
        return result
                    