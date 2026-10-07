class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            new_stone = stones.pop() - stones.pop()
            if new_stone:
                stones.append(new_stone)
        
        return stones[0] if stones else 0