class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = defaultdict(str)
        parents = {}

        for account in accounts:
            for i in range(1, len(account)):
                email_to_name[account[i]] = account[0]
                parents[account[i]] = account[i]
            
        def find(node):
            if parents[node] != node:
                parents[node] = find(parents[node])
            
            return parents[node]

        def union(a, b):
            parent_a = find(a)
            parent_b = find(b)

            if parent_a != parent_b:
                parents[parent_a] = parent_b

        for account in accounts:
            for i in range(2, len(account)):
                union(account[1], account[i])

        res = []
        merged = defaultdict(list)
        for email in parents:
            parent = find(email)
            merged[parent].append(email)
        
        for parent, emails in merged.items():
            res.append([email_to_name[parent]] + sorted(emails))

        return res

        
        