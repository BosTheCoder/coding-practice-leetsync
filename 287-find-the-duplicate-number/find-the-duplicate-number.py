class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast, slow = 0,0

        
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                break
        
        # print(f"fast {fast} slow {slow} met")

        fast = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]
        
        return fast