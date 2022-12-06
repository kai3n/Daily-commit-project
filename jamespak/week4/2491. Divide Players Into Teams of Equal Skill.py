class Solution:
    def dividePlayers(self, skill: List[int]) -> int:

        skill.sort()
        chemistry = skill[0] + skill[-1]
        total = 0
        left = 0
        right = len(skill) - 1

        while left < right:
            if skill[left] + skill[right] != chemistry:
                return -1
            total += skill[left]*skill[right]
            left += 1
            right -= 1
        return total
                
