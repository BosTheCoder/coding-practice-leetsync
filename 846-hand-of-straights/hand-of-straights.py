class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        num_groups = len(hand)/groupSize
        if num_groups % 1 != 0:
            return False

        num_groups = int(num_groups)
        hand.sort()
        
        arr = [[] for i in range(num_groups)]

        for i,card in enumerate(hand):
            appended = False
            for group in range(num_groups):
                if len(arr[group]) == groupSize:
                    continue
                if (
                    len(arr[group]) == 0
                    or
                    (len(arr[group]) > 0 and arr[group][-1] == card-1)
                ):
                    arr[group].append(card)
                    appended = True
                    break
            if not appended:
                return False
        return all(len(a)==groupSize for a in arr)    