class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0,0

        def nxt(i):
            return nums[i]
        
        while True:
            fast = nxt(nxt(fast))
            slow = nxt(slow)
            if fast == slow:
                break
        
        # print(f"fast {fast} slow {slow} met")

        fast = 0
        while fast != slow:
            fast = nxt(fast)
            slow = nxt(slow)
        
        return fast