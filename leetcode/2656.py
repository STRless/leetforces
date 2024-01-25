class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        pq = []
        for num in nums:
            heapq.heappush(pq, (-num))
        
        ans = 0
        while k:
            num = heapq.heappop(pq) * -1
            ans += num
            heapq.heappush(pq, (-(num+1)))
            k -= 1
        return ans