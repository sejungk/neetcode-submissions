class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        while len(stones) > 1:
            stone1 = stones.pop()
            stone2 = stones.pop()

            stones.append(abs(stone1 - stone2))
            stones.sort()
        
        if stones:
            return stones[0]
        else:
            return 0