class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = list(range(1, n + 1))
        i = 0
        while len(nums) > 1:
            i = (i + k - 1) % len(nums)
            nums.pop(i)
        return nums[0]

# O(n*k) solution
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = deque(range(1, n + 1))
        
        while len(q) > 1:
            x = k
            while x > 1:
                q.append(q.popleft())
                x -= 1
            q.popleft()
        return q[0]
