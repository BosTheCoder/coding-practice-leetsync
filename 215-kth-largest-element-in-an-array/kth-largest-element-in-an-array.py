class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def qs(arr, v):
            left, mid, right = [],[],[]
            pivot = random.choice(arr)
            for num in arr:
                if num == pivot:
                    mid.append(num)
                elif num>pivot:
                    left.append(num)
                else:
                    right.append(num)

            if v <= len(left):
                return qs(left, v)
            if v > len(left) + len(mid):
                return qs(right,v-len(left)-len(mid))
            else:
                return mid[0]

        return qs(nums,k)
