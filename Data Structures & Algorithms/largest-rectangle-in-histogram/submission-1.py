class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        
        for i in range(len(heights) + 1):
            curr_height = heights[i] if i < len(heights) else 0
            
            while stack and curr_height < heights[stack[-1]]:
                height = heights[stack.pop()]
                left_edge = stack[-1] + 1 if stack else 0
                width = i - left_edge 
                max_area = max(max_area, width * height)
            stack.append(i)

        return max_area