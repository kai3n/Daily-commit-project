class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        return True if "".join(next(zip(*words))) == s else False
