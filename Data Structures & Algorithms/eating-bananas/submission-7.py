class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2

            count = 0
            for pile in piles:
                count += math.ceil(float(pile) / mid)
            
            if count <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return left