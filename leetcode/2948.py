import heapq
class Node:
    def __init__(self, p, num):
        self.p = p
        self.rank = 0
        self.heap = [num]
    
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        n = len(nums)
        new_arr = [(i, nums[i])for i in range(n)]
        new_arr.sort(key=lambda x: (x[1], x[0]))
        subsets = [Node(i, nums[i]) for i in range(n)]

        def find(x):
            if subsets[x].p == x:
                return x
            subsets[x].p = find(subsets[x].p)
            return subsets[x].p
        
        def union(u, v):
            a, b = find(u), find(v)
            if subsets[a].rank < subsets[b].rank:
                subsets[a].p = b
                while subsets[a].heap:
                    heapq.heappush(subsets[b].heap, heapq.heappop(subsets[a].heap))
            else:
                subsets[b].p = a
                while subsets[b].heap:
                    heapq.heappush(subsets[a].heap, heapq.heappop(subsets[b].heap))
                if subsets[a].rank == subsets[b].rank:
                    subsets[a].rank += 1
        
        for i in range(1, n):
            if new_arr[i][1] - new_arr[i-1][1] <= limit:
                union(new_arr[i][0], new_arr[i-1][0])
        
        for i in range(n):
            p = find(i)
            
        ans = [0 for _ in range(n)]
        for i in range(n):
            p = find(i)
            ans[i] = heapq.heappop(subsets[p].heap)
        return ans