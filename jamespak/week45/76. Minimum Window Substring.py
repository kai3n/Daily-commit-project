class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_map = collections.Counter(t)

        count = len(t)
        start = end = head = 0
        min_substring_length = float('inf')

        while end < len(s):
            if target_map[s[end]] > 0:
                count -= 1
            target_map[s[end]] -= 1
            end += 1

            while count == 0:
                if (end - start) < min_substring_length:
                    min_substring_length = end - start
                    head = start
                target_map[s[start]] += 1

                if target_map[s[start]] > 0:
                    count += 1
                start += 1
        return "" if min_substring_length == float('inf') else s[head: head + min_substring_length]
