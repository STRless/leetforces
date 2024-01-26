class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        freq = [0 for _ in range(n)]
        adj = defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)
        
        def dfs(node, target, visit):
            if node == target:
                freq[node] += 1
                return True
            visit[node] = True
            for nei in adj[node]:
                if not visit[nei]:
                    flag = dfs(nei, target, visit)
                    if flag:
                        freq[node] += 1
                        return True
            return False
        
        for trip in trips:
            visit = [False for _ in range(n)]
            dfs(trip[0], trip[1], visit)
        
        @cache
        def dp(node=0, par=-1, flag=False):
            temp = freq[node] * price[node]
            if flag:
                temp //= 2
            for nei in adj[node]:
                if nei != par:
                    cur = float('inf')
                    if flag:
                        cur = min(cur, dp(nei, node, False))
                    else:
                        cur = min(cur, dp(nei, node, False))
                        cur = min(cur, dp(nei, node, True))
                    temp += cur
            return temp
        return min(dp(0, -1, True), dp(0, -1, False))