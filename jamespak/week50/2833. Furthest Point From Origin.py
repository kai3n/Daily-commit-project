class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        count = d = 0
        for move in moves:
            if move == "L":
                count -= 1
            elif move == "R":
                count += 1
            else:
                d += 1
        return abs(count) + d
