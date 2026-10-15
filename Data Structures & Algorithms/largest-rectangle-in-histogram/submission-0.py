class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i in range(len(heights) + 1):
            curr_height = heights[i] if i < len(heights) else 0

            while stack and heights[stack[-1]] > curr_height:
                height = heights[stack.pop()]
                left_edge = stack[-1] + 1 if stack else 0
                width = i - left_edge
                max_area = max(max_area, height * width)

            stack.append(i)
        return max_area