class TimeMap:

    def __init__(self):
        self.timemap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        curr = self.timemap.setdefault(key, [])
        curr.append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        curr = self.timemap.get(key,[])
        if not curr:
            return ""

        ix = bisect.bisect_left(curr, (timestamp,))
        if ix>=len(curr) or curr[ix][0] > timestamp:
            ix -= 1
        
        if ix<0 or curr[ix][0] > timestamp:
            return ""
        return curr[ix][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)