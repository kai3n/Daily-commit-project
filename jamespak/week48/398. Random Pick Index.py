class Solution:

    def __init__(self, nums):
        self.nums = nums
    
    def pick(self, target):
        k, res = 1, None
        
        for i, n in enumerate(self.nums):
            if n == target:
                if random.random() < 1/k:
                    res = i
                k += 1
        
        return res
