class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = Counter(hand)

        for start in sorted(counts):
            while counts[start] > 0:
                for val in range(start, start + groupSize):
                    if counts[val] == 0:
                        return False
                    counts[val] -= 1
        return True
            

            