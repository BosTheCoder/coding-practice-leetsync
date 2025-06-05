class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = Deque()
        ret = []

        for i, num in enumerate(nums):
            # if i == the delete point stored with the current max, popleft the max
            if q and q[0][1] == i:
                q.popleft()

            # while new num > end of q, pop the end of the queue. Then you can add new num
            while q and num>q[-1][0]:
                q.pop()
            q.append((num, i+k))

            # Save max
            if i>=k-1:
                ret.append(q[0][0])

        return ret