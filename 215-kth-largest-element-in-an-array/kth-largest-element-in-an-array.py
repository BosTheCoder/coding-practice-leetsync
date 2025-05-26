import random
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # we want the element whose rank in *descending* order is k-1
        target = k - 1
        lo, hi = 0, len(nums) - 1

        while True:
            # 1. choose a random pivot, swap it to the front for convenience
            pivot_idx = random.randint(lo, hi)
            pivot = nums[pivot_idx]
            nums[pivot_idx], nums[lo] = nums[lo], nums[pivot_idx]

            # 2. 3-way in-place partition:   >pivot | =pivot | <pivot
            gt, i, lt = lo, lo, hi                     # gt: next slot for >pivot
            while i <= lt:
                if nums[i] > pivot:                    # belongs in “greater”
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt += 1
                    i += 1
                elif nums[i] < pivot:                  # belongs in “less”
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt -= 1
                else:                                  # equal to pivot
                    i += 1

            # array now looks like:  [lo .. gt-1]  >p  |  [gt .. lt]  =p  |  [lt+1 .. hi]  <p
            left_size   = gt - lo          # number of >pivot elements
            mid_size    = lt - gt + 1      # number of =pivot elements

            if target < left_size:         # k-th largest is in the “greater” block
                hi = gt - 1
            elif target >= left_size + mid_size:
                lo = lt + 1
                target -= left_size + mid_size
            else:                          # inside the “equal” block → found it
                return pivot
