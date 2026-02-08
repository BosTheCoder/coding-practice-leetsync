class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        gt, eq , lt = [], [], []
        pivot = random.sample(nums,1)[0]

        print(nums, k, pivot)

        for val in nums:
            if val > pivot:
                gt.append(val)
            elif val == pivot:
                eq.append(val)
            else:
                lt.append(val)
            
        
        if k <= len(gt):
            return self.findKthLargest(gt, k)
        elif k <= len(gt) + len(eq):
            return eq[0]
        else:
            new_k = k-(len(gt) + len(eq))
            return self.findKthLargest(lt, new_k)
        