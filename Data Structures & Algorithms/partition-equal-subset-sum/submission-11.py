class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums) - 1, -1, -1):
            next_dp = dp.copy()
            for t in dp:
                if target == t + nums[i]:
                    return True
                next_dp.add(t + nums[i])

            dp = next_dp
        return False