class Solution:
    def ways(self, pizza: List[str], k: int) -> int:

        # From (x1, y1) To (x2, y2)
        @cache
        def check (x1,y1,x2,y2):
            for r in range(x1, x2+1):
                for c in range(y1, y2+1):
                    if pizza[r][c] == 'A':
                        return True 
            return False 
        
        @cache
        def dp (r, c, k):

            if k == 1 :
                if check (r, c, len(pizza)-1, len(pizza[0])-1):
                    return 1
            
            cnt = 0 
            for i in range(c+1, len(pizza[0])):
                if check (r, c, len(pizza)-1, i-1):
                    cnt += dp (r, i, k-1)
            for j in range(r+1, len(pizza)):
                if check (r, c, j-1, len(pizza[0])-1):
                    cnt += dp (j, c, k-1)
            return cnt 

        return dp(0,0,k) % (10 ** 9 + 7)
