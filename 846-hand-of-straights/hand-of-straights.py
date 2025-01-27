class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()
        groups = []
        for card in hand:
            suitable_group_ix = -1
            for ix, group in enumerate(groups):
                if card == group[-1]: 
                    continue
                if card != group[-1] + 1:
                    break
                group.append(card)
                suitable_group_ix = ix
                break

            if suitable_group_ix == -1:
                groups.append([card])
                suitable_group_ix = len(groups) - 1
            
            if len(groups[suitable_group_ix]) == groupSize:
                del groups[suitable_group_ix]
                
        # print(groups)
        return len(groups) == 0


"""
sort list first

figuring out which group to add the next number in the hand
- is the current group already finished
- is the number being added the same as the last one in the group?
  - if so skip group
- is the numner being added consecutive as the last one in the group?
  - If not skip group
- if no other groups then just start a new one

f there's anything left in groups thne false
"""