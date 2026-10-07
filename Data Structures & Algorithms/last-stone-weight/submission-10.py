class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_weight = max(stones)
        counts = [0] * (max_weight + 1)

        for weight in stones:
            counts[weight] += 1

        heaviest = max_weight
        while heaviest > 0:
            # Find the heaviest remaining stone.
            while heaviest > 0 and counts[heaviest] == 0:
                heaviest -= 1

            if heaviest == 0:
                return 0

            # Remove that stone.
            counts[heaviest] -= 1

            # Find the second heaviest stone start at the same weight
            second = heaviest
            while second > 0 and counts[second] == 0:
                second -= 1

            if second == 0:
                return heaviest

            # Remove the second stone.
            counts[second] -= 1

            difference = heaviest - second
            if difference > 0:
                counts[difference] += 1

            # All remaining stones are at or below this weight.
            heaviest = max(second, difference)

        return 0