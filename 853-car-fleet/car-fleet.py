class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sps = sorted(zip(position,speed))  # sorted positions and speeds
        # print(sps)
        time = [0] * len(position)
        for i,ps in enumerate(sps):
            p, s = ps
            time[i] = (target - p) / s
        # print(time)
        groups = 1
        curr = time[-1]
        # print("setting curr", curr)
        for i in range(len(speed)-2, -1, -1):
            if time[i] > curr:
                groups+=1
                curr = time[i]
                # print("setting curr", curr)
        
        return groups