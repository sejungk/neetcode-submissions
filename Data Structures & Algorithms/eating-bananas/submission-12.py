class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_num = max(piles)

        def eat_bananas(rate):
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / rate)
            return hours

        left = 1
        right = max_num

        while left < right:
            mid = (left + right) // 2

            if eat_bananas(mid) <= h:
                right = mid
            
            else:
                left = mid + 1
                
        return right