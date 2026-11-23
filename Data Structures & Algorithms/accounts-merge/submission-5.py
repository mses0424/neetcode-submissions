class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        n = len(accounts)
        parent = list(range(n))
        def find(x: int) -> int:
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]
        def union(x: int, y: int) -> None:
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        email_to_idx = {}
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_idx:
                    union(i, email_to_idx[email])
                else:
                    email_to_idx[email] = i
        root_to_emails = defaultdict(list)
        for email, idx in email_to_idx.items():
            root = find(idx)
            root_to_emails[root].append(email)
        result = []
        for root, emails in root_to_emails.items():
            name = accounts[root][0]
            result.append([name] + sorted(emails))

        return result