class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position,speed)))
        last_time = 0
        ret = set()
        for pos, s in reversed(cars):
            time_taken_without_blocker = (target-pos)/s    # works because python int division is floor
            time_taken_with_blocker = max(last_time, time_taken_without_blocker)
            ret.add(time_taken_with_blocker)
            last_time = time_taken_with_blocker
        # print(ret)
        return len(ret)

        

  