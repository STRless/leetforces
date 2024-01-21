class Solution:
    def countOfPairs(self, n: int, x: int, y: int) -> List[int]:
        ans = [0 for _ in range(n)]
        adj = defaultdict(list)
        for i in range(2, n+1):
            adj[i].append(i-1)
            adj[i-1].append(i)
        if x != y:
            adj[x].append(y)
            adj[y].append(x)
        
        distances = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
        
        for i in range(1, n+1):
            distances[i][i] = 0
            for nei in adj[i]:
                if distances[i][nei] > 1:
                    distances[i][nei] = 1
        
        for k in range(1, n+1):
            for i in range(1, n+1):
                for j in range(1, n+1):
                    if distances[i][j] > distances[i][k] + distances[k][j]:
                        distances[i][j] = distances[i][k] + distances[k][j]
        
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    dis = distances[i][j]
                    ans[dis-1] += 1
        return ans
                    
                
            