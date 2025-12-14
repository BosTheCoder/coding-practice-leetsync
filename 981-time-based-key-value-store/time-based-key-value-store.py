class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.d[key]
        
        ix = bisect.bisect_right(arr,timestamp, key=lambda x:x[0])

        if ix == 0:
            return ""
        return arr[ix-1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)