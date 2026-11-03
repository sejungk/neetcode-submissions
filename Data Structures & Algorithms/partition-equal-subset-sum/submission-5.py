class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for num in nums:
            next_dp = set()
            for t in dp:
                next_dp.add(t + num)
                next_dp.add(t)

                if t + num == target:
                    return True
                
                dp = next_dp
        
        return False
