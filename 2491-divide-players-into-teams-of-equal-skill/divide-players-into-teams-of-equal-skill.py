class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # If there's not an even number of skills
        if len(skill) % 2 != 0:
            return -1

        skill.sort()
        l = 0 
        r = len(skill) - 1

        ret = 0
        target = skill[r] + skill[l]
        while (
            l<r and
            r < len(skill) and
            l >= 0
        ):
            total = skill[r] + skill[l]
            if total != target:
                return -1
            
            ret += skill[r] * skill[l]

            l += 1
            r -= 1
        
        return ret


"""

[3,2,5,1,3,4]


"""