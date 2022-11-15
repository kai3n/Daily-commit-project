class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        if not self.d[key]:
            return ""

        i = bisect.bisect(self.d[key], timestamp, key=itemgetter(0))
        if not i: 
            return ""
        return self.d[key][i-1][1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

