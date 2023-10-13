class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        begin = end = res = count = 0
        
        while end < len(s):
            if d.get(s[end]) is not None:
                d[s[end]] += 1
                count += 1
            else:
                d[s[end]] = 1
            end += 1
            while count > 0:
                d[s[begin]] -= 1
                if d[s[begin]] == 0:
                    del d[s[begin]]
                elif d[s[begin]] == 1:
                    count -= 1
                begin += 1
            res = max(res, end - begin)
        return res
