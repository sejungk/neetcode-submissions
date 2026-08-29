class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque()

        left = 0
        right = 0
        while right < len(nums):
            #  remove all smaller nums in queue
            while q and nums[q[-1]] < nums[right]:
                q.pop()

            # add right val
            q.append(right)

            # remove left val from queue
            if left > q[0]:
                q.popleft()

            # only update output and move left if window is k
            if (right + 1) >= k:
                output.append(nums[q[0]])
                left += 1
            
            right += 1
        return output