class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        d = defaultdict(list)
        visited = set()
        res = []

        for account in accounts:
            for i in range(1, len(account) - 1):
                d[account[i]].append(account[i + 1])
                d[account[i + 1]].append(account[i])

        def dfs(email):
            visited.add(email)
            emails = [email]
            for e in d[email]:
                if e not in visited:
                    emails.extend(dfs(e))
            return emails
            
        for account in accounts:
            if account[1] not in visited:
                res.append([account[0]] + sorted(dfs(account[1])))
        return res
