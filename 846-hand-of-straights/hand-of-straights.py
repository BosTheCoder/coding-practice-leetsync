class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        counts = Counter(hand)
        heap = list(counts.keys())
        heapq.heapify(heap)

        while heap:
            smallest = heap[0]

            # try to create a group
            for i in range(groupSize):
                curr = smallest + i
                if curr in counts:
                    counts[curr] -= 1
                    if counts[curr] == 0:
                        if curr != heap[0]:
                            return False
                        heapq.heappop(heap)
                else:
                    return False
        return True

