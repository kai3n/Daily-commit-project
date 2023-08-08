class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        d1 = date(*tuple(int(val) for val in date1.split("-")))
        d2 = date(*tuple(int(val) for val in date2.split("-")))
        return abs((d1 - d2).days)
