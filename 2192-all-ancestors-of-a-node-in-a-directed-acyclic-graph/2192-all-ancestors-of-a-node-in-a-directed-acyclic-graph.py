class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = {k: set() for k in range(n)}
        pending = True
        while(pending):
            pending = False
            for x, y in edges:
                ol = len(ancestors[y])
                ancestors[y].add(x)
                if len(ancestors[x])>0:
                    ancestors[y] = ancestors[y].union(ancestors[x])
                nl = len(ancestors[y])
                if nl>ol:
                    pending = True
        for k in ancestors:
            ancestors[k] = list(ancestors[k])
            ancestors[k].sort()
        return list(ancestors.values())