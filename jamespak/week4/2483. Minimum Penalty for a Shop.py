class Solution(object):
    def bestClosingTime(self, customers):
        n = len(customers)
        penalty = customers.count('Y')
        if penalty == n: 
            return n
        cur_min, res = n, 0
        for i in range(len(customers)):
            if cur_min > penalty:
                cur_min = penalty
                res = i
            if customers[i] == 'Y':
                penalty -= 1
            else:
                penalty += 1
        if cur_min > penalty: return n
        return res
