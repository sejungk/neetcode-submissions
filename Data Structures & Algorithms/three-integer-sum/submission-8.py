class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        count = defaultdict(int)

        for num in nums:
            count[num] += 1

        res = []
        for i in range(n):
            count[nums[i]] -= 1
            if i and nums[i] == nums[i - 1]:
                continue
            
            for j in range(i + 1, n):
                count[nums[j]] -= 1
                if j - 1 > i and nums[j] == nums[j - 1]:
                    continue

                third = 0 - (nums[i] + nums[j])
                if count[third] > 0:
                    res.append([nums[i], nums[j], third])
            
            for j in range(i + 1, n):
                count[nums[j]] += 1
        return res

