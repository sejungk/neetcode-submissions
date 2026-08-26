class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        value_count = [[] for _ in range(len(nums) + 1)]
        for key, value in count.items():
            value_count[value].append(key)

        result = []
        for freq in range(len(value_count) -1, 0, -1):
            for num in value_count[freq]:
                result.append(num)
                k -= 1  
                if k == 0:
                    return result

