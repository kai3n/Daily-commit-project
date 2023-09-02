class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        prev = intervals[0]
        count = 0
        for interval in intervals[1:]:
            if interval[1] <= prev[1]:
                count += 1
                prev = interval
            elif interval[0] < prev[1] < interval[1]:
                count += 1
            else:
                prev = interval
        return count
