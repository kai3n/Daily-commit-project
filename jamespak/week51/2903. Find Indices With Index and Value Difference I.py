# O(n**2)
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        res = [-1, -1]
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                    res = [i, j]
        return res


# O(n)
class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        mini = maxi = 0
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < nums[mini]:
                mini = i - indexDifference
            if nums[i - indexDifference] > nums[maxi]:
                maxi = i - indexDifference
            if nums[i] - nums[mini] >= valueDifference:
                return [mini, i]
            if nums[maxi] - nums[i] >= valueDifference:
                return [maxi, i]
        return [-1, -1]
