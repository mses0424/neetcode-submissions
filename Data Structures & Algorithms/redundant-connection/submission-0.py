class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)+1))
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        for item in edges:
            first, second = item[0], item[1]
            root_f, root_s = find(first), find(second)
            if root_f == root_s:
                return [first,second]
            parent[root_s] = parent[root_f]