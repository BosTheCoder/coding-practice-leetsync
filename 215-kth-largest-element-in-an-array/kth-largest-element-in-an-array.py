class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def qs(arr, k):
            # get random pivot
            pivot = random.choice(arr)

            greater, lesser, equal = [],[],[]

            for num in arr:
                if num > pivot:
                    greater.append(num)
                elif num == pivot:
                    equal.append(num)
                else:
                    lesser.append(num)
            
            # Figure out where the kth largest element is

            if k <=len(greater):
                return qs(greater,k)
            elif k> len(greater) + len(equal):
                return qs(lesser,k-len(greater)-len(equal))
            else:
                return pivot

        return qs(nums,k)