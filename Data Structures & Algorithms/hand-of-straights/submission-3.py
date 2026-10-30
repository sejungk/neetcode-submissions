class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        counts = {}
        for card in hand:
            counts[card] = counts.get(card, 0) + 1

        # The heap tracks card values that still have copies.
        remaining_values = list(counts)
        heapq.heapify(remaining_values)

        while remaining_values:
            # A group must start with the smallest card still available.
            group_start = remaining_values[0]

            for card in range(group_start, group_start + groupSize):
                # This consecutive card must have an unused copy.
                if counts.get(card, 0) == 0:
                    return False

                counts[card] -= 1

                # When a card runs out, it should be the smallest remaining value.
                if counts[card] == 0:
                    if card != remaining_values[0]:
                        return False
                    heapq.heappop(remaining_values)

        return True