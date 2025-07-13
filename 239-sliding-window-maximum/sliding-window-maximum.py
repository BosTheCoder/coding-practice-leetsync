class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = Deque()
        maxw = [0] * (len(nums)-k+1)

        for i,num in enumerate(nums):
            if q and q[0][1] <= i:
                q.popleft()
            
            while q and q[-1][0] <= num:
                q.pop()
            
            q.append((num, i+k))

            if i >= k-1:
                maxw[i-k+1] = q[0][0]
        
        return maxw

