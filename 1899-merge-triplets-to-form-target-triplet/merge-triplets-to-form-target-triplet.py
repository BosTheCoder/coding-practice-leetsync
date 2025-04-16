from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = [False, False, False]
        for triplet in triplets:
            if all(triplet[i] <= target[i] for i in range(3)):
                for i in range(3):
                    if triplet[i] == target[i]:
                        good[i] = True
                if all(good):
                    return True  # Early exit!
        return all(good)

"""
1,2,5

[[2,5,3],[2,3,4],[1,2,5],[5,2,3],[6,5,5]],
"""