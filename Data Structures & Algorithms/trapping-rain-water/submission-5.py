class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n - 1

        res = 0
        max_left = height[l]
        max_right = height[r]
        while l <= r:
            if max_left < max_right:
                res += max(max_left - height[l], 0)
                max_left = max(max_left, height[l])
                l += 1
            else:
                res += max(max_right - height[r], 0)
                max_right = max(max_right, height[r])
                r -= 1

        return res
