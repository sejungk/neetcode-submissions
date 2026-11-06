class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num, count in counts.items():
            buckets[count].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            for num in buckets[i]:
                res.append(num)
                k -= 1
                if k == 0:
                    return res
