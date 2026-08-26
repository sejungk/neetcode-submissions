class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_vol = float("-inf")

        left = 0
        right = len(heights) - 1
        while left < right:
            curr = (right - left) * min(heights[left], heights[right])
            max_vol = max(curr, max_vol)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_vol

