class Logger:

    def __init__(self):
        self.d = collections.defaultdict(int)


    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.d.get(message, -1) == -1:
            self.d[message] = timestamp
            return True
        if self.d[message] + 10 <= timestamp:
            self.d[message] = timestamp
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
