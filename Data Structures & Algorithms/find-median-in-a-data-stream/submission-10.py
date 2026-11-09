class MedianFinder:

    def __init__(self):
        self.larger = []  # num [4, 5, 6, 7]
        self.smaller = [] # -num [-3, -2, -1]

    def addNum(self, num: int) -> None:
        # more nums in larger
        if len(self.larger) > len(self.smaller):
            if num < self.larger[0]:
                heapq.heappush(self.smaller, -num)
            else:
                removed_num = -heapq.heappop(self.larger)
                heapq.heappush(self.smaller, removed_num)
                heapq.heappush(self.larger, num)
         # equal nums in both
        else: 
            if len(self.smaller) == 0 or num > -self.smaller[0]:
                heapq.heappush(self.larger, num) 
            else:
                removed_num = -heapq.heappop(self.smaller)
                heapq.heappush(self.larger, removed_num)
                heapq.heappush(self.smaller, -num) 

    def findMedian(self) -> float:
        if len(self.larger) == len(self.smaller):
            num1 = self.larger[0]
            num2 = -self.smaller[0]
            return (num1 + num2) / 2

        else:
            return self.larger[0]
        