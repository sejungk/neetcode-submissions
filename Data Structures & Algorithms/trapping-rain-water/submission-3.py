class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left_max = [0] * n
        right_max = [0] * n

        max_height = 0
        for i in range(n):
            left_max[i] = max_height
            max_height = max(max_height, height[i])

        max_height = 0
        for i in range(n - 1, -1, -1):
            right_max[i] = max_height
            max_height = max(max_height, height[i])

        res = 0
        for i in range(n):
            curr = min(left_max[i], right_max[i]) - height[i]
            res += max(curr, 0)

        return res