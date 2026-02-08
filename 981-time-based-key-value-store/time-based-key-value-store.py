class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        
        # binary search
        arr = self.d[key]

        if not arr:
            return ""
        
        l = 0
        r = len(arr)
        while l<r:
            mid = l+(r-l)//2
            if arr[mid][0] >timestamp:
                r = mid
            else:
                l = mid+1

        if l >0:
            return arr[l-1][1]
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)