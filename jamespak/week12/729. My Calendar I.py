class MyCalendar:

    def __init__(self):
        self.calendar = []
        

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.calendar)):
            if self.calendar[i][0] <= start < self.calendar[i][1]:
                return False
            elif self.calendar[i][0] < end <= self.calendar[i][1]:
                return False
            elif start <= self.calendar[i][0] < end:
                return False
            elif start < self.calendar[i][1] <= end:
                return False
        self.calendar.append([start, end])
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)
