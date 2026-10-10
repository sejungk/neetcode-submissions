class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0

        for i in range(k + 1):
            tmp_prices = prices.copy()

            for source, dest, price in flights:
                if prices[source] == float("inf"):
                    continue
                if prices[source] + price < tmp_prices[dest]:
                    tmp_prices[dest] = prices[source] + price
            prices = tmp_prices
        return -1 if prices[dst] == float("inf") else prices[dst]