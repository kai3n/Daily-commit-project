from sortedcontainers import SortedList
class RangeModule:

    def __init__(self):
        self.ranges = SortedList()
        

    def addRange(self, left: int, right: int) -> None:
        insert_left = self.ranges.bisect_left(left)
        insert_right = self.ranges.bisect_right(right)
        #remove the ranges in between
        for _ in range(insert_right - insert_left):
            self.ranges.remove(self.ranges[insert_left])
        #check the boundary is out of exisitng ranges
        if insert_left % 2 == 0:
            self.ranges.add(left)
        if insert_right % 2 == 0:
            self.ranges.add(right)       
        

    def queryRange(self, left: int, right: int) -> bool:
        insert_left = self.ranges.bisect_right(left)
        insert_right = self.ranges.bisect_left(right)
        #check the boundary is within same exisitng ranges
        if insert_left == insert_right and insert_left % 2 == 1:
            return True
        else:
            return False

    def removeRange(self, left: int, right: int) -> None:
        insert_left = self.ranges.bisect_right(left)
        insert_right = self.ranges.bisect_left(right)
        for _ in range(insert_right - insert_left):
            self.ranges.remove(self.ranges[insert_left])
        #check the boundary is within exisitng ranges
        if insert_left % 2 == 1:
            self.ranges.add(left)
        if insert_right % 2 == 1:
            self.ranges.add(right)                 
            
            
# Your RangeModule object will be instantiated and called as such:
# obj = RangeModule()
# obj.addRange(left,right)
# param_2 = obj.queryRange(left,right)
# obj.removeRange(left,right)
