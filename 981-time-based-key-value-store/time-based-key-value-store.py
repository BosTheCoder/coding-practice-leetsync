class TimeMap:

    def __init__(self):
        self.timemap_dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timemap_dict:
            self.timemap_dict[key] = []

        self.timemap_dict[key].append((timestamp,value))


    def get(self, key: str, timestamp: int) -> str:
        ix = self.search(key, timestamp)
        if ix <1:
            return ""
        else:
            return self.timemap_dict[key][ix-1][1]
    
    
    def search(self, key:str, timestamp: int) -> int:
        """
        Return the index of the first value
        that was set at a timestamp larger than 
        provided timestamp using binary search.
        """
        if key not in self.timemap_dict:
            return 0
        arr = self.timemap_dict[key]
        l = 0
        r = len(arr)

        while l<r:
            mid = l + (r-l)//2
            mid_timestamp = arr[mid][0]
            if mid_timestamp > timestamp:
                r = mid
            else:
                l = mid+1
        
        return l
        

"""
0       T       T        T    = search(0)=0
1       F       T        T    = search(1)=1 
3       F       T        T    = search(1)=1
4       F       F        T    = search(4)=2
6       F       F        F    = search(6)=3
7       F       F        F
foo = [(1,bar),(4,bar2),(6,bar3)]


"""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)