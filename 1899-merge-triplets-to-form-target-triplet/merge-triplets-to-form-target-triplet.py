class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        relevant = []
        for triplet in triplets:
            if not any([val>target[i] for i,val in enumerate(triplet)]):
                relevant.append(triplet)

        count = 0

        for i in range(3):
            if any([triplet[i] == target[i] for triplet in relevant]):
                count+=1

        return count == 3
"""
1,2,5

[[2,5,3],[2,3,4],[1,2,5],[5,2,3],[6,5,5]],
"""