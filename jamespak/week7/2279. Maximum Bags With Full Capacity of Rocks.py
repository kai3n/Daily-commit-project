class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        remaining = [capacity[i] - rocks[i] for i in range(len(capacity))]
        remaining.sort()
        count = 0
        for i in range(len(remaining)):
            if remaining[i] <= 0:
                count += 1
            else:
                if additionalRocks - remaining[i] >= 0:
                    additionalRocks -= remaining[i]
                    count += 1
        return count
