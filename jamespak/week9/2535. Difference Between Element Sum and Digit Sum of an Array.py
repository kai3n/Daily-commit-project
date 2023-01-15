class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        digitSum = sum((map(int,list(''.join(map(str,nums))))))

        return sum(nums) - digitSum
