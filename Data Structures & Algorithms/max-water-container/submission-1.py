class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        max_vol = 0
        left = 0
        right = n-1

        while left < right:
            curr_vol = min(heights[left], heights[right]) * (right - left)
            max_vol = max(max_vol, curr_vol)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_vol
