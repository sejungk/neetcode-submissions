class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n

    def find(self, x):
        while x != self.par[x]:
            self.par[x] = self.par[self.par[x]]
            x = self.par[x]
        return self.par[x]

    def union(self, a, b):
        p1 = self.find(a)
        p2 = self.find(b)

        if p1 == p2:
            return False

        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        email_to_account = {}

        for i, a in enumerate(accounts):
            for e in a[1:]:
                if e in email_to_account:
                    uf.union(i, email_to_account[e])
                else:
                    email_to_account[e] = i
        
        email_group = defaultdict(list)
        for e, i in email_to_account.items():
            parent = uf.find(i)
            email_group[parent].append(e)
        
        res = []
        for i, emails in email_group.items():
            name = accounts[i][0]
            res.append([name] + sorted(email_group[i]))

        return res



