class TimeMap:

    def __init__(self):
        self.key_value = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key_value.setdefault(key, []).append((timestamp, value))
        self.key_value[key].sort()

    def get(self, key: str, timestamp: int) -> str:
        res_timestamp = float("-inf")
        res = ""

        if key in self.key_value:
            left = 0
            right = len(self.key_value[key]) - 1

            while left <= right:
                mid = (left + right) // 2

                t, v = self.key_value[key][mid]
           
                if t <= timestamp and t > res_timestamp:
                    res_timestamp = t
                    res = v
                    left = mid + 1
                else:
                    right = mid - 1

        
        if res == float("-inf"):
            return ""
        else:
            return res
