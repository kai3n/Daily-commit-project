class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            elif abbr[j] in "123456789":
                k = j
                n = ""
                while k < len(abbr) and abbr[k] in "0123456789":
                    n += abbr[k]
                    k += 1
                i += int(n)
                j = k
            else:
                return False
        return i == len(word) and j == len(abbr)
