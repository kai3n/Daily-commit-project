class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        bulky = heavy = False
        if any(x >= 10**4 for x in [length, width, height]) or length*width*height >= 10**9:
            bulky = True
        if mass >= 100:
            heavy = True
        if bulky and heavy:
            return "Both"
        elif not bulky and not heavy:
            return "Neither"
        elif bulky and not heavy:
            return "Bulky"
        else:
            return "Heavy"
        
