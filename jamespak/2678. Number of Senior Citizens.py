class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(True for detail in details if int(detail[11:13]) > 60)
