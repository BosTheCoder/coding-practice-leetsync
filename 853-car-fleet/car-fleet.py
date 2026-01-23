class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = list(zip(position,speed))
        position_speed.sort()

        times = [0] * len(position)
        for i, pos_speed in enumerate(position_speed):
            pos, speed = pos_speed
            time = (target - pos) / speed
            times[i] = time
        
        # print(times)
        groups = 0
        curr_largest = -float("inf")
        for i in range(len(position)-1, -1, -1):
            if times[i] > curr_largest:
                groups +=1
                curr_largest = times[i]
        
        return groups