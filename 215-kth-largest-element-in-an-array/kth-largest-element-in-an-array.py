class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        


        def dfs(arr, k):
            pivot = random.choice(arr)
            more, equal, less = [],[],[]

            for num in arr:
                if num == pivot:
                    equal.append(num)
                elif num > pivot:
                    more.append(num)
                else:
                    less.append(num)
            
            if k <= len(more):
                return dfs(more,k)
            elif k> (len(more) + len(equal)):
                return dfs(less, k-len(more)-len(equal))
            else:
                return equal[0]


        
        return dfs(nums, k)