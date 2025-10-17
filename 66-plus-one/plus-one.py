class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        overflow = 1
        q = deque([0] * len(digits))
        for i in range(len(digits)-1,-1,-1):
            total = overflow + digits[i]
            q[i] = total % 10
            overflow = total // 10

        if overflow:
            q.appendleft(overflow)

        return list(q)