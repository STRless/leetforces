class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        ans = 0
        check = {}
        for a, b in pairs:
            check[a] = b
            check[b] = a

        pos = [defaultdict(int) for _ in range(n)]
        for i, pref in enumerate(preferences):
            for j, p in enumerate(pref):
                pos[i][p] = j
        
        for i, pref in enumerate(preferences):
            y = check[i]
            for j, u in enumerate(pref):
                x = i
                v = check[u]
                if u == y:
                    break
                if pos[x][u] < pos[x][y] and pos[u][x] < pos[u][v]:
                    ans += 1
                    break
        
        return ans