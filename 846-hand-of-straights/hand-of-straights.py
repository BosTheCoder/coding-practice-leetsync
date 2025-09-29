class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = Counter(hand)
        heap = list(counts.keys())
        heapq.heapify(heap)

        while heap:
            val = heap[0]
            for i in range(groupSize):
                curr = val + i
                if (
                    curr not in counts or
                    counts[curr] == 0
                ): return False

                counts[curr] -= 1
                if counts[curr] == 0:
                    if heap[0] == curr:
                        heapq.heappop(heap)
                    else:
                        return False
        return True

"""

{1:1, 2:2, 3:2, 6:1, 4:1, 7:1, 8:1}




"""