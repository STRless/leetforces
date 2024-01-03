# Topics: Shortest Path
# Time Complexity: O(ElogV+N) where E is len(original), V is chars in original/changed, N is len(source)
# Space Complexity: O(2N) where N is len(source)
def get_idx(ch):
    return ord(ch) - ord('a')

class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adj = defaultdict(list)
        
        for i in range(len(original)):
            adj[original[i]].append((changed[i], cost[i]))
        
        dist = defaultdict(lambda: [float('inf') for _ in range(26)])
        
        for i in range(26):
            orig_ch = chr(ord('a') + i)
            pq = []
            heapq.heappush(pq, (0, orig_ch))
            dist[orig_ch][get_idx(orig_ch)] = 0
            while pq:
                cur_d, cur_ch = heapq.heappop(pq)
                for nei_ch, nei_d in adj[cur_ch]:
                    if cur_d + nei_d < dist[orig_ch][get_idx(nei_ch)]:
                        dist[orig_ch][get_idx(nei_ch)] = cur_d + nei_d
                        heapq.heappush(pq, (cur_d + nei_d, nei_ch))
                        
        ans = 0 
        for i in range(len(source)):
            if source[i] != target[i]:
                if dist[source[i]][get_idx(target[i])] == float('inf'):
                    return -1
                else:
                    ans += dist[source[i]][get_idx(target[i])]
        
        return ans