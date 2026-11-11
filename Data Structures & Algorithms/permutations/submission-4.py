class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        perms = [[]]

        for num in nums:
            new_perms = []
            for perm in perms:
                for i in range(len(perm) + 1):
                    copy = perm.copy()
                    copy.insert(i, num)
                    new_perms.append(copy)
            perms = new_perms
        return perms