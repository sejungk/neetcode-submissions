class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point):
            x, y = point
            return x ** 2 + y ** 2

        def partition(l, r):
            pivotIdx = r
            pivotDist = dist(points[pivotIdx])
            i = l
            for j in range(l, r):
                if dist(points[j]) <= pivotDist:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i
        
        L = 0
        R = len(points) - 1
        pivot = len(points)

        while pivot != k:
            pivot = partition(L, R)
            if pivot < k:
                L = pivot + 1
            else:
                R = pivot - 1
        
        return points[:k]

