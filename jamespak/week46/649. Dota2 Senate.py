class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = deque()
        r = deque()

        for i, p in enumerate(senate):
            if p == "R":
                r.append(i)
            else:
                d.append(i)
        
        while r and d:

            pr, pd = r.popleft(), d.popleft()
            if pr < pd:
                r.append(pr + len(senate))
            else:
                d.append(pd + len(senate))

        return "Radiant" if r else "Dire"
