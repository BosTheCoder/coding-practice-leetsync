class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        boxes = {}
        max_box = 0
        for i in range(lowLimit, highLimit+1):
            box = sum([int(c) for c in str(i)])
            boxes[box] = boxes.get(box,0) + 1
            max_box = max(max_box, boxes[box])
        return max_box