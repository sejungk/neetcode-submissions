class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        n = len(points)
        if k == n:
            return points

        l = 0
        r = n - 1
        while l <= r:
            partition = r
            p = l

            x1, y1 = points[partition]
            dist1 = math.sqrt((x1 * x1) + y1 * y1)

            start = l
            for i in range(l, r):
                x2, y2 = points[i]
                dist2 = math.sqrt((x2 * x2) + y2 * y2)

                if dist2 < dist1:
                    points[p], points[i] = points[i], points[p]
                    p += 1

            points[p], points[partition] = points[partition], points[p]

            if p == k - 1:
                break
            elif p > k - 1:
                r = p - 1
            else:
                l = p + 1

        return points[:p + 1]

            