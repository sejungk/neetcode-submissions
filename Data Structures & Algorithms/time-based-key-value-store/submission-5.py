class TimeMap:

    def __init__(self):
        self.items = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.items[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.items:
            return ""

        l = 0
        r = len(self.items[key]) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2
            if self.items[key][mid][0] <= timestamp:
                res = self.items[key][mid][1]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
