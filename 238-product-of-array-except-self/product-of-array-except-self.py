class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        l = [0]*length
        r = [0] * length

        l[0] = nums[0]
        for i in range(1,length):
            l[i] = l[i-1] * nums[i]


        r[-1] = nums[-1]
        for i in range(length-2,-1,-1):
            r[i] = r[i+1] * nums[i]


        prod = [0]* length
        for i in range(1, length-1):
            prod[i] = l[i-1] * r[i+1]
        prod[0] = r[1]
        prod[-1] = l[-2]
        return prod