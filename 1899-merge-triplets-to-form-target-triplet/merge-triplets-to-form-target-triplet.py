class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        count = [0,0,0]
        for triplet in triplets:
            if not any(val>target[i] for i,val in enumerate(triplet)):
                for i in range(3):
                    if triplet[i] == target[i]:
                        count[i] +=1
        return all(count[i] >= 1 for i in range(3))
"""
1,2,5

[[2,5,3],[2,3,4],[1,2,5],[5,2,3],[6,5,5]],
"""