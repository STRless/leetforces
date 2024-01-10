class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        comb = []
        temp = []

        def find_comb(i=0):
            if i == n:
                comb.append(temp.copy())
                return
            temp.append(i)
            find_comb(i+1)
            temp.pop()
            find_comb(i+1)

        def is_under_max_distance(no_visit, start):
            distances = [float('inf') for _ in range(n)]
            pq = []
            heapq.heappush(pq, (0, start))
            distances[start] = 0
            
            while pq:
                dis, cur = heapq.heappop(pq)
                for nei in range(n):
                    if adj[cur][nei] != float('inf') and nei not in no_visit:
                        if dis + adj[cur][nei] < distances[nei]:
                            distances[nei] = dis + adj[cur][nei]
                            heapq.heappush(pq, (dis + adj[cur][nei], nei))

            for i in range(n):
                if distances[i] == float('inf') and i not in no_visit:
                    return False
                if distances[i] != float('inf') and distances[i] > maxDistance:
                    return False
            return True

        find_comb()

        adj = [[float('inf') for _ in range(n)] for _ in range(n)]
        for a, b, c in roads:
            adj[a][b] = min(adj[a][b], c)
            adj[b][a] = min(adj[b][a], c)
        
        ans = 0
        for closed_set in comb:
            flag = True
            for i in range(n):
                if i not in closed_set:
                    flag &= is_under_max_distance(closed_set, i)
            if flag:
                ans += 1
                
        return ans