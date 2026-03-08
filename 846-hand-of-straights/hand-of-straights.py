class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        counter = Counter(hand)

        heap = list(counter.keys())
        heapq.heapify(heap)

        while heap:
            min_val = heap[0]

            for i in range(min_val, min_val+groupSize):
                if i not in counter:
                    return False
                
                counter[i] -=1

                if counter[i] == 0:
                    # try to pop the same value from heap
                    if heap[0] != i:
                        return False
                    heapq.heappop(heap)
                    del counter[i]
        
        return True
                