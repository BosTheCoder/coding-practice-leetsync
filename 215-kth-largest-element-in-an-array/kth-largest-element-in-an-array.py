class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def qs(arr, ix):
            pivot = random.choice(arr)
            larger, smaller, equal = [],[],[]
            for num in arr:
                if num<pivot:
                    smaller.append(num)
                elif num == pivot:
                    equal.append(num)
                else:
                    larger.append(num)


            len_of_larger = len(larger)
            if ix <= len_of_larger:
                return qs(larger,ix)
            
            len_of_combined = len_of_larger + len(equal)
            if ix > len_of_combined:
                return qs(smaller, ix - len_of_combined)
            
            return pivot
        

        return qs(nums,k)