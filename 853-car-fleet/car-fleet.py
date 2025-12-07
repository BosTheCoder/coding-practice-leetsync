class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        vectors = list(zip(position,speed))
        vectors.sort()
        
        curr_max = 0
        groups = 0
        for pos, speed in reversed(vectors):
            time = (target-pos)/speed
            
            if time > curr_max:
                curr_max = time
                groups += 1
        
        return groups