class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        res = 0

        while mainTank >= 5:
            res += 50
            mainTank -= 5
            if additionalTank >= 1:
                mainTank += 1
                additionalTank -= 1
        res += mainTank*10
        return res
