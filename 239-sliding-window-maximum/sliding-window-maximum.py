class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        q = Deque()
        l = 0
        ret = []
        for r,num in enumerate(nums):
            # shorten window to what's valid
            if r-l+1 > k:
                l += 1

            # clear queue of old numbers (we should only need to pop one)
            if q and q[0][1] < l:
                q.popleft()
            

            # handling the new number...
            # if it's greater, we clear until we reach a num that's larger than it
            # if it's less then we append
            while q and num>q[-1][0]:
                q.pop()
            q.append((num,r))


            # add to return array if length is long enough
            if r-l+1 == k:
                ret.append(q[0][0])
        
        return ret
            


"""
q = (1,0) 
window length = r-1 + 1 = 3

1   l
3   r
-1 
-3  r
5
3
6
7

"""