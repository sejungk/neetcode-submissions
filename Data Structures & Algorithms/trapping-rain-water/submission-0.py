class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        total = 0
        left_heights = [(0, 0)] * n
        right_heights = [(0, 0)] * n
        max_height = 0
        max_idx = 0

        for i in range(n):
            left_heights[i] = (max_height, max_idx)

            if height[i] > max_height:
                max_height = height[i]
                max_idx = i

        max_height = 0
        max_idx = n-1
        for i in range(n-1, -1, -1):
            right_heights[i] = (max_height, max_idx)

            if height[i] > max_height:
                max_height = height[i]
                max_idx = i

        for i in range(n):
            left_max_height, _ = left_heights[i]
            right_max_height, _ = right_heights[i]

            water = min(left_max_height, right_max_height) - height[i]

            if water > 0:
                total += water
        
        return total