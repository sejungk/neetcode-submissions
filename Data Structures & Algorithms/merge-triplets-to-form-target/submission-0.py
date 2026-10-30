class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        candidates = []
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            candidates.append(t)

        a = False
        b = False
        c = False
        for t in candidates:
            if t[0] == target[0]:
                a = True
            if t[1] == target[1]:
                b = True
            if t[2] == target[2]:
                c = True
            
            if a and b and c:
                return True
        
        return False