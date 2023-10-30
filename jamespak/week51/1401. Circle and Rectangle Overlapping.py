class Solution:
    def checkOverlap(self, r: int, x_c: int, y_c: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        corners = [(x1,y1), (x2,y1), (x2,y2), (x1, y2)]
        for (x, y) in corners:
            if (x_c - x)**2 + (y_c - y)**2 <= r**2:
                return True

        for x in [x1, x2]:
            if x_c-r <= x <= x_c+r and y1<=y_c<=y2:
                return True
        for y in [y1, y2]:
            if y_c-r <= y <= y_c+r and x1<=x_c<=x2:
                return True

        if x1<=x_c<=x2 and y1<=y_c<=y2:
            return True
        return False
